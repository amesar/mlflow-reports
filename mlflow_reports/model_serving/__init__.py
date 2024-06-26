# https://mlflow.org/docs/latest/python_api/mlflow.deployments.html#mlflow.deployments.DatabricksDeploymentClient

import os
from mlflow.deployments.mlflow import MlflowDeploymentClient
from mlflow.deployments.databricks import DatabricksDeploymentClient
from mlflow.deployments import get_deploy_client
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common.pandas_utils import move_column
from mlflow_reports.client.model_serving_client import ModelServingClient


CUSTOM_MODEL = "CUSTOM_MODEL" # note that endpoint type is not set for custom model
FOUNDATION_MODEL = "FOUNDATION_MODEL"
EXTERNAL_MODEL = "EXTERNAL_MODEL"
FEATURE_SPEC = "FEATURE_SPEC"


def get_endpoint_client(use_deployment_client=False):
    if use_deployment_client:
        client = get_deploy_client(os.environ.get("MLFLOW_TRACKING_URI"))
    else:
        client = ModelServingClient()
    print("Model serving endpoint client:", type(client))
    return client


def get_endpoints(model_type=None, use_deployment_client=False):
    """
    Get model server endpoints from either Databricks or OSS Mlflow.
    """
    client = get_endpoint_client(use_deployment_client)
    endpoints = client.list_endpoints()

    if isinstance(client, MlflowDeploymentClient):
        endpoints = _MlflowDeploymentClient_to_dict(endpoints)
    elif isinstance(client, DatabricksDeploymentClient):
        pass
    elif isinstance(client, ModelServingClient):
        endpoints = endpoints["endpoints"]
    else:
        raise MlflowReportsException(message=f"Unsupported Deployment client: {type(client)}")

    if model_type == "custom":
        return [ ep for ep in endpoints if not ep.get("endpoint_type") ]
    elif model_type == "external":
        return [ ep for ep in endpoints if ep.get("endpoint_type") == "EXTERNAL_MODEL" ]
    elif model_type == "foundation":
        return [ ep for ep in endpoints if ep.get("endpoint_type") == "FOUNDATION_MODEL_API" ]

    return endpoints


def get_entities(endpoint):
    config = endpoint.get("config", {})
    return config.get("served_entities", [])

def filter_entities(entities, entity_type=None):
    if entity_type == CUSTOM_MODEL: # Custom models don't have a type field set
        return [ ent for ent in entities if not ent.get("type") ]
    else:
        return [ ent for ent in entities if ent.get("type") == entity_type ]


def as_pandas_df(endpoints):
    from mlflow_reports.list import list_utils
    import pandas as pd
    import numpy as np
    df = pd.DataFrame.from_dict(endpoints)
    df = df.replace(np.nan, "", regex=True)
    list_utils.to_datetime(df, ["creation_timestamp", "last_updated_timestamp"])
    df = move_column(df, "endpoint_type", index=1)
    return df


def _MlflowDeploymentClient_to_dict(endpoints):
    """
    Convert mlflow.deployments.mlflow.MlflowDeploymentClient to a dict
    """
    def convert(ep): # mlflow.deployments.server.config.Endpoint
        _ep = { k:v for k,v in ep.__dict__.items() if k not in ["model", "limit"] }
        _ep["model"] = { k:v for k,v in ep.model.__dict__.items() } # mlflow.gateway.config.RouteModelInfo
        if ep.limit: # mlflow.gateway.config.Limit
            limit = { k:v for k,v in ep.limit.__dict__.items() }
            _ep["limit"] = limit
        return _ep
    return [ convert(ep) for ep in endpoints ]


def get_openapi_schema(client, endpoint_name):
    try:
        return client.get_endpoint_openapi_schema(endpoint_name)
    except MlflowReportsException as e:
        return { "error": str(e) }

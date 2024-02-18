
import os
from mlflow.deployments.mlflow import MlflowDeploymentClient
from mlflow.deployments.databricks import DatabricksDeploymentClient
from mlflow.deployments import get_deploy_client
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.client.model_serving_client import ModelServingClient


def get_endpoint_client(use_databricks=False):
    if use_databricks:
        client = ModelServingClient()
    else:
        client = get_deploy_client(os.environ.get("MLFLOW_TRACKING_URI"))
    print("Model serving endpoint client:", type(client))
    return client


def get_endpoints(call_databricks_model_serving=False):
    client = get_endpoint_client(call_databricks_model_serving)
    endpoints = client.list_endpoints()
    if isinstance(client, MlflowDeploymentClient):
        endpoints = _MlflowDeploymentClient_to_dict(endpoints)
    elif isinstance(client, DatabricksDeploymentClient):
        pass
    elif isinstance(client, ModelServingClient):
        endpoints = endpoints["endpoints"]
    else:
        raise MlflowReportsException(message=f"Unsupported Deployment client: {type(client)}")
    return endpoints


def _MlflowDeploymentClient_to_dict(endpoints):
    """
    Convert mlflow.deployments.mlflow.MlflowDeploymentClient to dict
    """
    def convert(ep): # mlflow.deployments.server.config.Endpoint
        _ep = { k:v for k,v in ep.__dict__.items() if k not in ["model", "limit"] }
        _ep["model"] = { k:v for k,v in ep.model.__dict__.items() } # mlflow.gateway.config.RouteModelInfo
        if ep.limit: # mlflow.gateway.config.Limit
            limit = { k:v for k,v in ep.limit.__dict__.items() }
            _ep["limit"] = limit
        return _ep
    return [ convert(ep) for ep in endpoints ]

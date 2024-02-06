"""
Create and show a Pandas dataframe and text table fromt the JSON response for all endpoints.
"""

import click

from mlflow.deployments.mlflow import MlflowDeploymentClient
from mlflow.deployments.databricks import DatabricksDeploymentClient

from mlflow_reports.client.model_serving_client import ModelServingClient
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common.click_options import opt_output_file_base
from mlflow_reports.common import io_utils
from mlflow_reports.list.click_options import opt_columns
from . click_options import opt_call_databricks_model_serving
from . import get_endpoint_client


def list_endpoints(columns, output_file_base, call_databricks_model_serving):
    client = get_endpoint_client(call_databricks_model_serving)
    endpoints = client.list_endpoints()
    if isinstance(client, MlflowDeploymentClient):
        endpoints = _to_dict(endpoints)
        ts_columns = []
    elif isinstance(client, DatabricksDeploymentClient):
        ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    elif isinstance(client, ModelServingClient):
        endpoints = endpoints["endpoints"]
        ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    else:
        raise MlflowReportsException(message=f"Unsupported Deployment client: {type(client)}")
    io_utils.write_csv_and_json_files(output_file_base, endpoints, columns, ts_columns)


def _to_dict(endpoints):
    def convert(ep): # mlflow.deployments.server.config.Endpoint
        _ep = { k:v for k,v in ep.__dict__.items() if k not in ["model", "limit"] }
        _ep["model"] = { k:v for k,v in ep.model.__dict__.items() } # mlflow.gateway.config.RouteModelInfo
        if ep.limit: # mlflow.gateway.config.Limit
            limit = { k:v for k,v in ep.limit.__dict__.items() }
            _ep["limit"] = limit
        return _ep
    return [ convert(ep) for ep in endpoints ]


@click.command()
@opt_columns
@opt_output_file_base
@opt_call_databricks_model_serving
def main(columns, output_file_base, call_databricks_model_serving):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    list_endpoints(columns, output_file_base, call_databricks_model_serving)


if __name__ == "__main__":
    main()

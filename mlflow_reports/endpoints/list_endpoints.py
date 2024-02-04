"""
Create and show a Pandas dataframe and text table fromt the JSON response for all endpoints.
"""

import click
import pandas as pd

from mlflow_reports.common import MlflowReportsException
from mlflow_reports.list.click_options import opt_columns, opt_output_csv_file
from mlflow_reports.list import list_utils
from . click_options import opt_call_databricks_model_serving
from . import get_endpoint_client

from mlflow.deployments.mlflow import MlflowDeploymentClient
from mlflow.deployments.databricks import DatabricksDeploymentClient


def create_pandas_df(call_databricks_model_serving=False):
    client = get_endpoint_client(call_databricks_model_serving)
    endpoints = client.list_endpoints()
    if isinstance(client, MlflowDeploymentClient):
        endpoints = _to_dict(endpoints)
        df = pd.json_normalize(endpoints)
    elif isinstance(client, DatabricksDeploymentClient):
        if isinstance(endpoints, dict): # NOTE: Databricks api/2.0/serving-endpoints returns dict and not list
            endpoints = endpoints["endpoints"]
        df = pd.json_normalize(endpoints)
        list_utils.to_datetime(df, "creation_timestamp")
        list_utils.to_datetime(df, "last_updated_timestamp")
    else:
        raise MlflowReportsException(message=f"Unsupported MLflow Deployments client: {type(client)}")
    return df


def _to_dict(endpoints):
    def convert(ep):
        _ep = { k:v for k,v in ep.model.__dict__.items() if k != "model" }
        model = { k:v for k,v in ep.model.__dict__.items() }
        _ep["model"] = model
        return _ep
    return [ convert(ep) for ep in endpoints ]


@click.command()
@opt_columns
@opt_output_csv_file
@opt_call_databricks_model_serving
def main(columns, output_csv_file, call_databricks_model_serving):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    df = create_pandas_df(call_databricks_model_serving)
    print(f"Found {df.shape[0]} endpoints")
    if isinstance(columns, str):
        columns = columns.split(",")
    list_utils.show_and_write(df, columns, output_csv_file)

if __name__ == "__main__":
    main()

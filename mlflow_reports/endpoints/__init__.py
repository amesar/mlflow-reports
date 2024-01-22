
import os
from mlflow_reports.client.model_serving_client import ModelServingClient
from mlflow.deployments import get_deploy_client


def get_endpoint_client(use_databricks=False):
    if use_databricks:
        client = ModelServingClient()
    else:
        client = get_deploy_client(os.environ.get("MLFLOW_TRACKING_URI"))
    print("Endpoint client:", type(client))
    return client

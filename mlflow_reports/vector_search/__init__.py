from databricks.vector_search.client import VectorSearchClient
from mlflow_reports.client import mlflow_auth_utils


def get_VectorSearchClient():
    host, token = mlflow_auth_utils.get_mlflow_host_token()
    return VectorSearchClient(disable_notice=True, workspace_url=host, personal_access_token=token)

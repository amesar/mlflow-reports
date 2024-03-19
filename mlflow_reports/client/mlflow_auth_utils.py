import os
import mlflow
from mlflow_reports.client import databricks_cli_utils
from mlflow_reports.common import MlflowReportsException


def get_mlflow_host():
    """ Returns the MLflow tracking URI (host) """
    return get_mlflow_host_token()[0]


def get_mlflow_host_token():
    """
    Returns the MLflow tracking URI (host) and Databricks personal access token (PAT).
    For Databricks there are two environment variable choices:
       - MLFLOW_TRACKING_URI - profile - the MLflow tracking URI in the form of 'databricks' or 'databricks://MY_PROFILE'.
       - DATABRICKS_HOST (e.g. https://e2-demo-west.cloud.databricks.com) and DATABRICKS_TOKEN
    """

    dbx_host = os.environ.get("DATABRICKS_HOST")
    dbx_token = os.environ.get("DATABRICKS_TOKEN")
    if dbx_host and dbx_token:
        return (dbx_host, dbx_token)

    uri = mlflow.tracking.get_tracking_uri()
    if uri:
        if not uri.startswith("databricks"):
            if not uri.startswith("http"):
                _raise_exception(uri)
            else:
                return (uri, None)
    else:
        _raise_exception(uri)

    try:
        toks = uri.split("//")
        profile = uri.split("//")[1] if len(toks) > 1 else None
        return databricks_cli_utils.get_host_token_for_profile(profile)
    # databricks_cli.utils.InvalidConfigurationError
    # requests.exceptions.InvalidSchema(f"No connection adapters were found for {url!r}")
    except Exception as e:
        print(f"WARNING: {e}")
        return (None, None)


def _raise_exception(uri):
    raise MlflowReportsException(message=f"MLflow tracking URI (MLFLOW_TRACKING_URI environment variable) must be an HTTP URI: '{uri}'")

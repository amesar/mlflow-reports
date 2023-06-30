from mlflow_reports.client.http_client import MlflowHttpClient
from mlflow.utils.databricks_utils import is_in_databricks_runtime, get_workspace_info_from_dbutils

http_client = MlflowHttpClient()

_workspace_host, _workspace_id = get_workspace_info_from_dbutils()

_UI_LINK_TAG = "_web_ui_link"

def add_run_link(run):
    info = run["info"]
    experiment_id = info["experiment_id"]
    run_id = info["run_id"]
    link = f"{_mk_mlflow_link()}/experiments/{experiment_id}/runs/{run_id}"
    run["info"][_UI_LINK_TAG] = link


def add_experiment_link(exp):
    link = f'{_mk_mlflow_link()}/experiments/{exp["experiment_id"]}'
    exp[_UI_LINK_TAG] = link


def add_model_version_link(version):
    link = f'{_mk_mlflow_link()}/models/{version["name"]}/versions/{version["version"]}'
    version[_UI_LINK_TAG] = link


def add_registered_model_link(reg_model):
    link = f'{_mk_mlflow_link()}/models/{reg_model["name"]}'
    reg_model[_UI_LINK_TAG] = link


def _mk_mlflow_link():
    client_uri = (str(http_client))
    idx = client_uri.find("/api/")
    mlflow_uri = client_uri[0:idx]
    if _workspace_host: # inside Databricks, e.g. "https://c3-south.mist.databricks.com"
         mlflow_uri = f"{_workspace_host}#mlflow"
    else:
        if not http_client.token: # calling OSS server
            mlflow_uri += "#" # for open source
        else: # calling Databricks externally
            mlflow_uri += "#mlflow"
    return mlflow_uri 

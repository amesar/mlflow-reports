from mlflow_reports.client.http_client import get_mlflow_client
from mlflow.utils.databricks_utils import get_workspace_info_from_dbutils

http_client = get_mlflow_client()

_workspace_host, _workspace_id = get_workspace_info_from_dbutils()

_UI_LINK_TAG = "_web_ui_link"
_API_LINK_TAG= "_api_link"

def add_run_links(run):
    info = run["info"]
    experiment_id = info["experiment_id"]
    run_id = info["run_id"]
    link = f"{_mk_mlflow_link()}/experiments/{experiment_id}/runs/{run_id}"
    run["info"][_UI_LINK_TAG] = link
    link = f"{http_client}/runs/get?run_id={run_id}"
    run["info"][_API_LINK_TAG] = link


def add_experiment_links(exp):
    experiment_id = exp["experiment_id"]
    link = f"{_mk_mlflow_link()}/experiments/{experiment_id}"
    exp[_UI_LINK_TAG] = link
    link = f"{http_client}/experiments/get?experiment_id={experiment_id}"
    exp[_API_LINK_TAG] = link


def add_model_version_links(version):
    name = version["name"]
    vr = version["version"]
    link = f"{_mk_mlflow_link()}/models/{name}/versions/{vr}"
    version[_UI_LINK_TAG] = link
    link = f"{http_client}/model-versions/get?name={name}&version={vr}"
    version[_API_LINK_TAG] = link


def add_registered_model_links(reg_model):
    name = reg_model["name"]
    link = f"{_mk_mlflow_link()}/models/{name}"
    reg_model[_UI_LINK_TAG] = link
    link = f"{http_client}/registered-models/get?name={name}"
    reg_model[_API_LINK_TAG] = link


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

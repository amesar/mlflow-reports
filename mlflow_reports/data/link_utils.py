from mlflow.utils.databricks_utils import get_workspace_info_from_dbutils
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.mlflow_utils import is_unity_catalog_model


mlflow_client = get_mlflow_client()

_workspace_host, _workspace_id = get_workspace_info_from_dbutils()

_UI_LINK_TAG = "_web_ui_link"
_API_LINK_TAG= "_api_link"


# == MLflow object linkers

def add_run_links(run):
    info = run["info"]
    experiment_id = info["experiment_id"]
    run_id = info["run_id"]
    link = f"{_get_mlflow_ui_base()}/experiments/{experiment_id}/runs/{run_id}"
    run["info"][_UI_LINK_TAG] = link
    link = f"{mlflow_client.get_api_uri()}/runs/get?run_id={run_id}"
    run["info"][_API_LINK_TAG] = link


def add_experiment_links(exp):
    experiment_id = exp["experiment_id"]
    link = f"{_get_mlflow_ui_base()}/experiments/{experiment_id}"
    exp[_UI_LINK_TAG] = link
    link = f"{mlflow_client.get_api_uri()}/experiments/get?experiment_id={experiment_id}"
    exp[_API_LINK_TAG] = link


def add_model_version_links(version):
    _mk_uc_links(version, version["name"], version["version"])


def add_registered_model_links(reg_model):
    _mk_uc_links(reg_model, reg_model["name"])


# == Helpers

def _mk_uc_links(dct, model_name, version=None):
    from requests.utils import quote
    from urllib.parse import urlencode

    _model_name = quote(model_name)
    if is_unity_catalog_model(model_name):
        _model_name = _model_name.replace(".","/")
        ui_link = f"{_get_host_name()}/explore/data/models/{_model_name}"
        uc_component = "unity-catalog/"
        vresource = "version"
    else:
        ui_link = f"{_get_mlflow_ui_base()}/models/{_model_name}"
        uc_component = ""
        vresource = "versions"

    params = { "name": model_name }
    if version:
        resource = "model-versions"
        params["version"] = version
        ui_link += f"/{vresource}/{version}"
    else:
        resource = "registered-models"
    qp = urlencode(params)
    api_link = f"{mlflow_client.get_api_uri()}/{uc_component}{resource}/get?{qp}"

    dct[_UI_LINK_TAG] = ui_link
    dct[_API_LINK_TAG] = api_link

def _get_mlflow_ui_base():
    """
    OSS:        http://localhost:5020#
    Databricks: https://e2-demo-west.cloud.databricks.com#mlflow
    """
    mlflow_uri = _get_host_name()
    if _workspace_host: # inside Databricks, e.g. "https://c3-south.mist.databricks.com"
        mlflow_uri = f"{_workspace_host}#mlflow"
    else:
        if not mlflow_client.get_token(): # calling MLflow OSS tracking server
            mlflow_uri += "#" # for open source
        else: # calling Databricks externally
            mlflow_uri += "#mlflow"
    return mlflow_uri

def _get_host_name():
    """
    OSS:        http://localhost:5020
    Databricks: https://e2-demo-west.cloud.databricks.com
    """
    client_uri = mlflow_client.get_api_uri()
    idx = client_uri.find("/api/")
    return client_uri[0:idx]

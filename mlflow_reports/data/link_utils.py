from mlflow.utils.databricks_utils import get_workspace_info_from_dbutils
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.mlflow_utils import is_unity_catalog_model

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
    model_name = version["name"]
    vr = version["version"]
    if is_unity_catalog_model(model_name):
        ui_link = f"{_mk_uc_model_ui_uri(model_name)}/version/{vr}"
        uc_component = "unity-catalog"
    else:
        ui_link = f"{_mk_mlflow_link()}/models/{model_name}/versions/{vr}"
        uc_component = ""
    version[_UI_LINK_TAG] = ui_link
    api_link = f"{_get_api_uri()}/{uc_component}model-versions/get?name={model_name}&version={vr}"
    version[_API_LINK_TAG] = api_link


def add_registered_model_links(reg_model):
    model_name = reg_model["name"]
    if is_unity_catalog_model(model_name):
        ui_link = _mk_uc_model_ui_uri(model_name)
        uc_component = "unity-catalog"
    else:
        ui_link = f"{_mk_mlflow_link()}/models/{model_name}"
        uc_component = ""
    reg_model[_UI_LINK_TAG] = ui_link
    api_link = f"{_get_api_uri()}/{uc_component}/registered-models/get?name={model_name}"
    reg_model[_API_LINK_TAG] = api_link


def _mk_uc_model_ui_uri(model_name):
    # TODO: need to add "?o={workspace_id}"
    # https://e2-demo-west.cloud.databricks.com/explore/data/models/my_catalog.default.my_model
    return f"{_get_host_name()}/explore/data/models/{model_name}"

def _get_api_uri():
    """
    MLflow API base: https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow
    """
    from mlflow_reports.client.http_client import UnityCatalogHttpClient
    if isinstance(http_client, UnityCatalogHttpClient):
        return str(http_client._mlflow_client)
    else:
        return str(http_client)

def _get_host_name():
    """
    Workspace host name: https://e2-demo-west.cloud.databricks.com
    """
    client_uri = _get_api_uri()
    idx = client_uri.find("/api/")
    return client_uri[0:idx]

def _mk_mlflow_link():
    mlflow_uri = _get_host_name()
    if _workspace_host: # inside Databricks, e.g. "https://c3-south.mist.databricks.com"
        mlflow_uri = f"{_workspace_host}#mlflow"
    else:
        if not http_client.get_token(): # calling MLflow OSS tracking server
            mlflow_uri += "#" # for open source
        else: # calling Databricks externally
            mlflow_uri += "#mlflow"
    return mlflow_uri

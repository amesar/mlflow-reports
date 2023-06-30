from mlflow_reports.client.http_client import MlflowHttpClient

http_client = MlflowHttpClient()

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
    #mlflow_uri += "#" # TODO: for open source
    mlflow_uri += "#mlflow"
    return mlflow_uri 

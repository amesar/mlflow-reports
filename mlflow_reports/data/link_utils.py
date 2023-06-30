from mlflow_reports.client.http_client import MlflowHttpClient

http_client = MlflowHttpClient()


def add_run_link(run):
    info = run["info"]
    experiment_id = info["experiment_id"]
    run_id = info["run_id"]
    link = f"{_mk_mlflow_link()}/experiments/{experiment_id}/runs/{run_id}"
    run["info"]["_run_ui_link"] = link


def add_experiment_link(exp):
    link = f'{_mk_mlflow_link()}/experiments/{exp["experiment_id"]}'
    exp["_experiment_ui_link"] = link


def add_model_version_link(version):
    link = f'{_mk_mlflow_link()}/models/{version["name"]}/versions/{version["version"]}'
    version["_model_version_ui_link"] = link


def add_registered_model_link(reg_model):
    link = f'{_mk_mlflow_link()}/models/{reg_model["name"]}'
    reg_model["_registered_model_ui_link"] = link


def _mk_mlflow_link():
    client_uri = (str(http_client))
    idx = client_uri.find("/api/")
    mlflow_uri = client_uri[0:idx]
    #mlflow_uri += "#" # TODO: for open source
    mlflow_uri += "#mlflow"
    return mlflow_uri 

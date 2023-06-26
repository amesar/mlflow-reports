from mlflow_reports.client.http_client import MlflowHttpClient
from mlflow_reports.common import mlflow_utils

http_client = MlflowHttpClient()


def split_model_uri(model_uri):
    """
    Splits an MLflow model URI into two parts
      - For models scheme, returns the model name and stage or version, e.g models:/sklearn_wine/production
      - For runs scheme, returns the run ID relative model path, e.g runs:/2079b9ee113b4b6c8ae631790d4c1009/sklearn-model
    :param: Models URI.
    :return: Tuple of model name and stage/version or tuple of run ID and relative model path.
    """
    idx = model_uri.find("/")
    path = model_uri[idx+1:]
    idx = path.find("/")
    return path[:idx], path[idx+1:]


def get_model_and_version(model_uri, get_permissions=False):
    """ 
    Get model and version number for a model version URI  
    """
    model_name, version_or_stage = split_model_uri(model_uri)
    version = _get_version(model_name, version_or_stage)
    reg_model = mlflow_utils.get_registered_model(model_name, get_permissions)
    return reg_model, version


def _get_version(model_name, version_or_stage):
    """ 
    Get version number for a version_or_stage 
    """
    if version_or_stage.isdigit():
        rsp = http_client.get(f"model-versions/get", {"name": model_name, "version": version_or_stage} )
        return rsp["model_version"]
    else:
        rsp = http_client.get(f"registered-models/get-latest-versions", {"name": model_name, "stages": [version_or_stage]} )
        versions = rsp["model_versions"]
        if len(versions) == 0:
            raise RuntimeError(f"No '{version_or_stage}' stage for model '{model_name}/{version_or_stage}'")
        return versions[0]


def get_reg_model_download_uri(version):
    """
    Return the download URI of the MLflow model in the registry
    """
    rsp = http_client.get("model-versions/get-download-uri", {"name": version["name"], "version": version["version"] })
    return rsp.get("artifact_uri")


def get_run_model_download_uri(version):
    """
    Return the download URI of the MLflow model in the run
    """
    return version["source"]


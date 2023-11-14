import mlflow
from mlflow.artifacts import download_artifacts
from mlflow.utils.file_utils import TempDir

from mlflow_reports.common import io_utils
from mlflow_reports.common import explode_utils


def get_model_info(model_uri):
    """
    Returns dictionary representation of MLflow MLmodel file (analagous to ModelInfo object)
    """
    model_info = get_model_artifact(model_uri, "MLmodel", file_type="yaml", explode_json=True)
    enrich_model_info(model_info)
    return model_info


def get_model_artifact(model_uri, artifact_path, file_type=None, explode_json=True):
    """
    Returns contents of an artifact as a Python object.
    """

    artifact_uri = f"{model_uri}/{artifact_path}"
    try:
        with TempDir() as tmp:
            local_path = download_artifacts(artifact_uri=artifact_uri, dst_path=tmp.path())
            dct = io_utils.read_file(local_path, file_type=file_type)
            if explode_json:
                explode_utils.explode_json(dct)
            return dct
    except mlflow.exceptions.RestException as e:
        msg = f"Cannot download artifact '{artifact_uri}'. Exception: {e}."
        print(f"WARNING: {msg}")
        return { "warning": msg }


def enrich_model_info(model_info):
    """
    Add native model flavor as 'model_flavor" attribute to model_info
    """
    flavors = model_info.get("flavors")
    if flavors:
        flavor_names = list(model_info["flavors"].keys())
        if len(flavor_names) == 1:
            flavor = flavor_names[0]
        else:
            flavors = [ f for f in flavor_names if f != "python_function" ]
            flavor = flavors[0]
        model_info["model_flavor"] = flavor
    else:
        model_info["flavors"] = { "warning": "No flavors" }


def mk_run_uri(run_id, artifact_path):
    return f"runs:/{run_id}/{artifact_path}"

def mk_run_download_uri(run, artifact_path):
    return f'{run["info"]["artifact_uri"]}/{artifact_path}'

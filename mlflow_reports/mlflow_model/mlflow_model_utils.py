from mlflow.artifacts import download_artifacts
from mlflow.utils.file_utils import TempDir

from mlflow_reports.common import io_utils
from mlflow_reports.common import explode_utils


def get_model_info(model_uri):
    """ 
    Returns dictionary representation of MLflow MLmodel file (analagous to ModelInfo object)
    """
    return get_model_artifact(model_uri, "MLmodel", file_type="yaml", explode_json=True)


def get_model_artifact(model_uri, artifact_path, file_type=None, explode_json=True):
    """
    Returns contents of an artifact as a Python object.
    """
    with TempDir() as tmp:
        artifact_uri = f"{model_uri}/{artifact_path}"
        local_path = download_artifacts(artifact_uri=artifact_uri, dst_path=tmp.path())
        dct = io_utils.read_file(local_path, file_type=file_type)
        if explode_json:
            explode_utils.explode_json(dct)
        return dct


def mk_run_uri(run_id, artifact_path):
    return f"runs:/{run_id}/{artifact_path}"

def mk_run_download_uri(run, artifact_path):
    return f'{run["info"]["artifact_uri"]}/{artifact_path}'

import click
import mlflow

from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common import (
    model_version_utils,
    timestamp_utils,
    io_utils
)
from mlflow_reports.common.click_options import(
    opt_model_uri,
    opt_get_permissions,
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import get_mlflow_model as _get_mlflow_model
from mlflow_reports.data import (
    get_registered_model,
    get_model_version,
    get_experiment ,
    get_run 
)
from mlflow_reports.data import local_utils # TODO: move to common
from . mlflow_model_utils import mk_run_uri, mk_run_download_uri


def get(
        model_uri, 
        get_permissions = False, 
        get_raw = False,
    ):
    """
    Return Data class object.
    """
    if model_uri.startswith("data:/"):
        data = _get_data_from_file(model_uri)
    else:
        data = _get_data_from_api(model_uri, get_permissions, get_raw)
    return data


def _get_data_from_api(model_uri, get_permissions=False, get_raw=False):
    scheme = _get_scheme(model_uri)
    _mlflow_model = _get_mlflow_model.get(model_uri, get_raw=get_raw)
    mlflow_model = _mlflow_model.get("mlflow_model")
    if not mlflow_model:
        return _mlflow_model

    run_id = mlflow_model.get("run_id")
    run_uri = mk_run_uri(run_id, mlflow_model.get("artifact_path"))
    
    model_uris = { 
        "model_uri": model_uri,
        "run_uri": run_uri,
    }
    if scheme == "models":
        registered_model, model_version = model_version_utils.get_model_and_version(model_uri, get_permissions=get_permissions)
        get_registered_model.enrich(registered_model, get_permissions=get_permissions)
        registered_model.pop("latest_versions", None) # NOTE: don't need this for our current purposes
        get_model_version.enrich(model_version)
        _run_id = model_version["run_id"]
        assert run_id == _run_id 
        model_uris["reg_model_download_uri"] = model_version.get("_reg_model_download_uri")
        #model_uris["run_model_download_uri"] = model_version.get("_run_model_download_uri")
    else:
        registered_model = None
        model_version = None

    try:
        run = get_run.get(run_id, get_raw=get_raw)
        run = run["run"]
        experiment = get_experiment.get(run["info"]["experiment_id"], get_permissions=get_permissions, get_raw=get_raw)
        experiment = experiment["experiment"]
        model_uris["run_model_download_uri"] = mk_run_download_uri(run, mlflow_model.get("artifact_path"))
    except MlflowReportsException as e:
        msg = { "model_uri": model_uri, "run_id": run_id }
        print(f"ERROR: Cannot get run: {msg}. Exception: {e}")
        run = { "error": str(e) }
        experiment = None

    manifest = {
        "model_uri": model_uri,
        "source": mlflow.get_tracking_uri(),
        "model_uris": model_uris,
        "mlflow_version": mlflow.__version__,
        "timestamp": timestamp_utils.ts_now_fmt_utc
    }

    dct = {
        "manifest": manifest,
        "mlflow_model": mlflow_model,
        "run": run,
        "experiment": experiment,
    }
    if registered_model:
        dct["registered_model"] = registered_model
    if model_version:
        dct["model_version"] = model_version
    mlflow_model_raw = _mlflow_model.get("mlflow_model_raw")
    if mlflow_model_raw:
        dct["mlflow_model_raw"] = mlflow_model_raw
    return dct


def _get_data_from_file(data_path):
    """
    Experimental.
    """
    data_path = data_path.replace("data:/","")
    dct = io_utils.read_file(data_path)
    dct["manifest"]["source"] = data_path
    return dct


def _get_scheme(path):
    if ":" in path:
        return path.split(":")[0]
    else:
        return None


@click.command()
@opt_model_uri
@opt_get_permissions
@opt_get_raw
@opt_silent
@opt_output_file

def main(model_uri, get_permissions, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(model_uri, get_permissions, get_raw)
    local_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

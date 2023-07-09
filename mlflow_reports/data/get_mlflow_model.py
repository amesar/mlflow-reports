import click
from mlflow_reports.mlflow_model import mlflow_model_utils
from mlflow_reports.data import get_run as _get_run
from mlflow_reports.data import get_experiment as _get_experiment
from mlflow_reports.common.click_options import(
    opt_model_uri,
    opt_get_run,
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import data_utils


def get(
        model_uri, 
        get_run = False, 
        get_raw = False, 
    ):
    model_info = mlflow_model_utils.get_model_info(model_uri)
    if not isinstance(model_info, dict):
        # NOTE: maybe raise exception instead of return
        return { 
            "error": f"Failed to parse MLmodel file of '{model_uri}'",
            "contents": str(model_info)
        }
    dct = { "mlflow_model": model_info }
    model_info_raw = _get_raw_model(model_uri, model_info)
    if model_info_raw:
        dct["mlflow_model_raw"] = model_info_raw
    if get_run:
        rsp = _get_run.get(model_info["run_id"], get_raw=get_raw)
        run = rsp["run"]
        dct["run"] = run
        rsp = _get_experiment.get(run["info"]["experiment_id"], get_raw=get_raw)
        dct["experiment"] = rsp["experiment"]
    return dct


def _get_raw_model(model_uri, model_info):
    """
    If this is a feature store model, then we process data/feature_store/raw_model/MLmodel.
    """
    flavors = model_info.get("flavors")
    if len(flavors) > 1:
        return None
    pyfunc = flavors["python_function"]
    lm = pyfunc.get("loader_module")
    if lm == "mlflow.pyfunc.model":
        return None
    if lm == "databricks.feature_store.mlflow_model":
        subdir = "data/feature_store"
        fs_spec = model_info = mlflow_model_utils.get_model_artifact(model_uri, f"{subdir}/feature_spec.yaml")
        fs_model_info = mlflow_model_utils.get_model_artifact(model_uri, f"{subdir}/raw_model/MLmodel", file_type="yaml")
        return {
            "model_type": "feature_store",
            "mlflow_model": fs_model_info,
            "feature_spec": fs_spec
        }
    else:
        return {
            "model_type": "unknown",
            "loader_module": lm
        }


@click.command()
@opt_model_uri
@opt_get_run
@opt_get_raw
@opt_silent
@opt_output_file

def main(model_uri, get_run, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(model_uri, get_run, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

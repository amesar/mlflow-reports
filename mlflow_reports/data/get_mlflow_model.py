import click

from mlflow_reports.client.http_client import MlflowHttpClient
from mlflow_reports.data import mlflow_model
from mlflow_reports.data import get_run as _get_run
from mlflow_reports.data import get_experiment as _get_experiment
from mlflow_reports.common.click_options import(
    opt_model_uri,
    opt_get_run,
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import local_utils

http_client = MlflowHttpClient()


def get(
        model_uri, 
        get_run = False, 
        get_raw = False, 
    ):
    model_info = mlflow_model.get_model_info(model_uri)
    dct = {
        "mlflow_model": model_info
    }
    if get_run:
        rsp = _get_run.get(model_info["run_id"], get_raw=get_raw)
        run = rsp["run"]
        dct["run"] = run
        rsp = _get_experiment.get(run["info"]["experiment_id"], get_raw=get_raw)
        dct["experiment"] = rsp["experiment"]
    return dct


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
    local_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

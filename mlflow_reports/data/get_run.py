import click

from mlflow_reports.client.http_client import MlflowHttpClient
from mlflow_reports.common import mlflow_utils, explode_utils
from mlflow_reports.common.click_options import(
    opt_run_id,
    opt_get_raw,
    opt_artifact_max_level,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import local_utils

http_client = MlflowHttpClient()


def get(run_id, artifact_max_level=-1, get_raw=False):
    """
    Gets full run details including optionally a list of artifacts.
    :return: Dictionary with "run" and optionally "artifacts" key
    """
    rsp = http_client.get(f"runs/get", { "run_id": run_id })
    if get_raw:
        return rsp
    return enrich(rsp["run"], artifact_max_level, get_raw)


def enrich(run, artifact_max_level=-1, get_raw=False):
    """
    Enrich the raw run API response.
    :return: Dictionary with "run" and optionally "artifacts" key
    """
    dct = { "run": run }
    if artifact_max_level > 0:
        artifacts = mlflow_utils.build_artifacts(run["info"]["run_id"], "", artifact_max_level)
        dct["artifacts"] = artifacts

    if not get_raw:
        _adjust_times(run)
        local_utils.mk_tags(run["data"])
        explode_utils.explode_json(dct)
    return dct


def _adjust_times(run):
    info = run["info"]
    local_utils.adjust_ts(info,["start_time", "end_time"])
    start = info.get("start_time")
    end = info.get("end_time")
    if start and end:
        dur = float(int(end) - int(start))/1000
        info["_duration"] = dur
    exp = http_client.get("experiments/get", {"experiment_id": info["experiment_id"]}) ["experiment"]
    run["info"]["_experiment_name"] = exp["name"]


@click.command()
@opt_run_id
@opt_artifact_max_level
@opt_get_raw
@opt_silent
@opt_output_file

def main(run_id, artifact_max_level, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(run_id, artifact_max_level, get_raw)
    local_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

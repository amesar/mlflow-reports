import click

from mlflow_reports.client.http_client import MlflowHttpClient
from mlflow_reports.common import mlflow_utils
from mlflow_reports.common import explode_utils 
from mlflow_reports.common.click_options import(
    opt_run_id,
    opt_dump_raw,
    opt_artifact_max_level,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import local_utils

http_client = MlflowHttpClient()


def get(
        run_id, 
        artifact_max_level = -1, 
        dump_raw = False, 
        silent = True, 
        output_file = None
    ):
    """
    Gets full run details including optionally a list of artifacts.
    """
    rsp = http_client.get(f"runs/get", { "run_id": run_id })
    run = rsp["run"]
    return adapt(run, artifact_max_level, dump_raw, silent, output_file)


def adapt(run, artifact_max_level=-1, dump_raw=False, silent=True, output_file=None):
    run_id = run["info"]["run_id"]
    dct = { "run": run }

    if artifact_max_level > -1:
        artifacts = mlflow_utils.build_artifacts(run_id, "", artifact_max_level)
        dct["artifacts"] = artifacts

    if not dump_raw:
        _adjust_times(run)
        local_utils.mk_tags(run["data"])
        explode_utils.explode_json(dct)

    local_utils.finish(dct, output_file, silent)
    return dct


def _adjust_times(run):
    info = run["info"]
    local_utils.adjust_ts(info,["start_time", "end_time"])
    start = info.get("start_time")
    end = info.get("end_time")
    if start and end:
        dur = float(int(end) - int(start))/1000
        info["_duration"] = dur


@click.command()
@opt_run_id
@opt_artifact_max_level
@opt_dump_raw
@opt_silent
@opt_output_file

def main(run_id, artifact_max_level, dump_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    get(run_id, artifact_max_level, dump_raw, silent, output_file)


if __name__ == "__main__":
    main()

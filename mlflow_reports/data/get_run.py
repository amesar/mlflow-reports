import click

from mlflow_reports.client import mlflow_client
from mlflow_reports.common import mlflow_utils, explode_utils
from mlflow_reports.common.click_options import(
    opt_run_id,
    opt_get_raw,
    opt_artifact_max_level,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import data_utils, link_utils
from mlflow_reports.data import enriched_tags


def get(run_id, artifact_max_level=-1, get_raw=False):
    """
    Gets full run details including optionally a list of artifacts.
    :return: Dictionary with "run" and optionally "artifacts" key
    """
    rsp = mlflow_client.get_run(run_id)
    if get_raw:
        return rsp
    return enrich(rsp["run"], artifact_max_level)


def enrich(run, artifact_max_level=-1):
    """
    Enrich the raw run API response.
    :return: Dictionary with "run" and optionally "artifacts" key
    """
    dct = { "run": run }
    if artifact_max_level > 0:
        artifacts = mlflow_utils.build_artifacts(run["info"]["run_id"], "", artifact_max_level)
        dct["artifacts"] = artifacts

    _adjust_times(run)
    link_utils.add_run_links(run)
    data_utils.mk_tags(run["data"])
    explode_utils.explode_json(dct)

    return dct


def _adjust_times(run):
    info = run["info"]
    data_utils.adjust_ts(info,["start_time", "end_time"])
    start = info.get("start_time")
    end = info.get("end_time")
    if start and end:
        dur = float(int(end) - int(start))/1000
        info[enriched_tags.TAG_DURATION] = dur
    exp = mlflow_client.get_experiment(info["experiment_id"])["experiment"]
    run["info"][enriched_tags.TAG_EXPERIMENT_NAME] = exp["name"]


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
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

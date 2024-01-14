import click
import mlflow

from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.data import get_run as _get_run
from mlflow_reports.common import mlflow_utils
from mlflow_reports.common import permissions_utils
from mlflow_reports.common import explode_utils
from mlflow_reports.common.http_iterators import SearchRunsIterator
from mlflow_reports.common.click_options import(
    opt_experiment_id_or_name,
    opt_get_runs,
    opt_get_permissions,
    opt_get_raw,
    opt_artifact_max_level,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import data_utils, link_utils
from mlflow_reports.data import enriched_tags

mlflow_client = get_mlflow_client()


def get(
        experiment_id_or_name, 
        get_runs = False, 
        get_permissions = False, 
        artifact_max_level = -1, 
        get_raw = False, 
    ):
    exp = mlflow_utils.get_experiment(experiment_id_or_name)
    experiment_id = exp["experiment_id"]

    rsp = mlflow_client.get(f"experiments/get", { "experiment_id": experiment_id })
    if get_raw:
        return rsp

    experiment = rsp["experiment"]
    dct = { "experiment": experiment }
    if get_runs:
        runs = SearchRunsIterator(mlflow_client, [experiment_id])
        dct["runs"] = [ _get_run.enrich(run, artifact_max_level=artifact_max_level) for run in runs ]
    enrich(experiment, get_permissions)

    return dct


def enrich(exp, get_permissions=False):
    data_utils.mk_tags(exp)
    data_utils.adjust_ts(exp, ["creation_time", "last_update_time"])
    exp[enriched_tags.TAG_TRACKING_URI] = mlflow.get_tracking_uri()
    link_utils.add_experiment_links(exp)
    explode_utils.explode_json(exp)
    if get_permissions:
        permissions_utils.add_experiment_permissions(exp)


@click.command()
@opt_experiment_id_or_name
@opt_get_runs
@opt_get_permissions
@opt_artifact_max_level
@opt_get_raw
@opt_silent
@opt_output_file
def main(experiment_id_or_name, get_runs, get_permissions, artifact_max_level, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(experiment_id_or_name, get_runs, get_permissions, artifact_max_level, get_raw)
    data_utils.dump_object(dct, output_file, silent) 

if __name__ == "__main__":
    main()

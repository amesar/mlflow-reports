"""
Get the latest run (by start_time) of an experiment.
"""

import click
from mlflow_reports.common.click_options import (
    opt_experiment_id_or_name, opt_output_file,
    opt_get_raw, opt_artifact_max_level
)
from mlflow_reports.data import data_utils
from mlflow_reports.common.mlflow_utils import get_latest_run
from mlflow_reports.data import get_run


def get(experiment_id_or_name, artifact_max_level, get_raw):
    run = get_latest_run(experiment_id_or_name)
    if run:
        return get_run.get(run["info"]["run_id"], artifact_max_level, get_raw)
    else:
        print(f"WARNING: No run found for experiment '{experiment_id_or_name}'")
    return run


@click.command()
@opt_experiment_id_or_name
@opt_artifact_max_level
@opt_get_raw
@opt_output_file
def main(experiment_id_or_name, artifact_max_level, get_raw, output_file):
    """
    Get the latest model version of a registered model.
    """
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    vr = get(experiment_id_or_name, artifact_max_level, get_raw)
    if vr:
        data_utils.dump_object(vr, output_file, silent=False)


if __name__ == "__main__":
    main()


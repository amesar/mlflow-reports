"""
Get the latest model version
"""

import click
from mlflow_reports.common.click_options import (
    opt_registered_model, opt_output_file,
    opt_get_expanded, opt_get_raw
)
from mlflow_reports.data import data_utils
from mlflow_reports.common.model_version_utils import get_latest_model_version
from mlflow_reports.data import get_model_version


def get(model_name, get_expanded, get_raw):
    vr = get_latest_model_version(model_name)
    if vr:
        return get_model_version.get(vr["name"], vr["version"], get_expanded, get_raw)
    else:
        print(f"WARNING: No model versions found for registered model '{model_name}'")
    return vr


@click.command()
@opt_registered_model
@opt_get_expanded
@opt_get_raw
@opt_output_file
def main(registered_model, get_expanded, get_raw, output_file):
    """
    Get the latest model version of a registered model.
    """
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    vr = get(registered_model, get_expanded, get_raw)
    if vr:
        data_utils.dump_object(vr, output_file, silent=False)


if __name__ == "__main__":
    main()


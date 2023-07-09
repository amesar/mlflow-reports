import click

from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common import mlflow_utils
from mlflow_reports.common import permissions_utils
from mlflow_reports.common.click_options import(
    opt_registered_model,
    opt_get_permissions,
    opt_get_run,
    opt_artifact_max_level,
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import get_run, get_model_version
from mlflow_reports.data import local_utils, link_utils


def get(
        model_name, 
        get_run = False, 
        artifact_max_level = -1,
        get_permissions = False, 
        get_raw = False, 
    ):
    reg_model = mlflow_utils.get_registered_model(model_name, get_permissions)
    if get_raw:
        return { "registered_model": reg_model } # To be compatible with API response

    dct = { "registered_model": reg_model }
    enrich(reg_model, get_permissions)
    if get_run:
        dct = _fetch_runs(reg_model, artifact_max_level)
    return dct


def enrich(reg_model, get_permissions=False):
    reg_model["tags"] = mlflow_utils.mk_tags_dict(reg_model.get("tags"))
    local_utils.adjust_ts(reg_model, [ "creation_timestamp", "last_updated_timestamp" ])
    link_utils.add_registered_model_links(reg_model)
    versions = reg_model.get("latest_versions") # NOTE: In UC, this is null, otherwise an array
    if versions:
        for vr in versions:
            get_model_version.enrich(vr)
    else:
        pass # TODO - all versions
        print(f"WARNING: Unity catalog registered model '{reg_model['name']}' does got support 'latest_versions()'")
    if get_permissions and "id" in reg_model:  # if calling Databricks tracking server
        permissions_utils.add_model_permissions(reg_model)
    return reg_model


def _fetch_runs(reg_model, artifact_max_level):
    dct = { "registered_model": reg_model }
    runs = {}
    vrs = reg_model.get("latest_versions")
    if vrs:
        for vr in vrs:
            try:
                runs[vr["version"]] = get_run.get(vr["run_id"], artifact_max_level=artifact_max_level) 
            except MlflowReportsException as e:
                msg = { "model": vr["name"], "version": vr["version"], "run_id": vr["run_id"] }
                print(f"ERROR: Cannot get run for {msg}. Exception: {e}")
        dct["version_runs"] = runs
    else:
        print(f"WARNING: Unity catalog registered model '{reg_model['name']}' does got support 'latest_versions()'")
    return dct


@click.command()
@opt_registered_model
@opt_get_run
@opt_artifact_max_level 
@opt_get_permissions
@opt_get_raw
@opt_silent
@opt_output_file
def main(registered_model, get_run, artifact_max_level, get_permissions, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(registered_model, get_run, artifact_max_level, get_permissions, get_raw)
    local_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

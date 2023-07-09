import click

from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common.model_version_utils import get_reg_model_download_uri, get_run_model_download_uri
from mlflow_reports.common import mlflow_utils
from mlflow_reports.common.click_options import(
    opt_registered_model,
    opt_model_version,
    opt_get_run,
    opt_artifact_max_level,
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import get_run as _get_run
from mlflow_reports.data import data_utils, link_utils

http_client = get_mlflow_client()


def get(
        registered_model_name, 
        version, 
        get_run = False, 
        artifact_max_level = -1,
        get_raw = False,
    ):
    rsp = http_client.get(f"model-versions/get", {"name": registered_model_name, "version": version} )
    if get_raw:
        return rsp
    version = rsp["model_version"]
    dct = {
        "model_version": version
    }
    enrich(version)
    if get_run:
        _get_vr_run(dct, artifact_max_level)
    return dct


def enrich(version):
    if mlflow_utils.is_calling_databricks():
        try:
            rsp = http_client.get(f"transition-requests/list", {"name": version['name'], "version": version['version']} )
            if rsp:
                version["transition_requests"] = rsp["requests"]
        except MlflowReportsException as e:
            print(f"WARNING: Databricks API call failed: {e}")

    data_utils.mk_tags(version)
    data_utils.adjust_ts(version, [ "creation_timestamp", "last_updated_timestamp" ])
    version["_reg_model_download_uri"] = get_reg_model_download_uri(version)
    version["_run_model_download_uri"] = get_run_model_download_uri(version)
    link_utils.add_model_version_links(version)


def _get_vr_run(dct, artifact_max_level):
    vr = dct["model_version"]
    try:
        dct["run"] = _get_run.get(vr["run_id"], artifact_max_level=artifact_max_level)
    except Exception as e:
        print(f'ERROR: Cannot get run {vr["run_id"]} for version {vr["version"]}. Exception: {e}')


@click.command()
@opt_registered_model
@opt_model_version
@opt_get_run
@opt_artifact_max_level 
@opt_get_raw
@opt_silent
@opt_output_file
def main(registered_model, version, get_run, artifact_max_level, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(registered_model, version, get_run, artifact_max_level, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

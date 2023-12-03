import click
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.data import get_experiment
from mlflow_reports.data import get_registered_model
from mlflow_reports.mlflow_model.mlflow_model_utils import get_model_artifact
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common.model_version_utils import get_reg_model_download_uri, get_run_model_download_uri
from mlflow_reports.common import mlflow_utils, explode_utils, exception_utils
from mlflow_reports.common.click_options import(
    opt_registered_model,
    opt_model_version,
    opt_get_expanded,
    opt_artifact_max_level,
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from mlflow_reports.data import get_run as _get_run
from mlflow_reports.data import data_utils, link_utils
from mlflow_reports.data import enriched_tags

http_client = get_mlflow_client()


def get(
        registered_model_name,
        version,
        get_expanded = False,
        get_raw = False,
        artifact_max_level = -1,
    ):
    """
    :param model_name: Registered model name.
    :param version: Registered model version.
    :param get_expanded: Returns graph of related objects: mlflow model (MLmodel file), run, experiment and registered model.
    :param get_raw: Return only the original raw model version.
    :param artifact_max_level: Number of artifact levels to recurse for run artifacts.
    :return: Returns model version object.
    """
    rsp = http_client.get(f"model-versions/get", {"name": registered_model_name, "version": version} )
    if get_raw:
        return rsp
    vr = rsp["model_version"]
    enrich(vr)
    dct = { "model_version": vr }
    if get_expanded:
        dct["mlflow_model"] = _get_mlmodel(registered_model_name, version)
        dct["registered_model"] = get_registered_model.get(registered_model_name, get_permissions=True)
        get_registered_model.enrich(dct["registered_model"]["registered_model"])
        _get_vr_run(dct, artifact_max_level)
    return dct


def enrich(vr):
    data_utils.mk_tags(vr)
    if mlflow_utils.is_calling_databricks() and not mlflow_utils.is_unity_catalog_model(vr["name"]):
        try:
            rsp = http_client.get(f"transition-requests/list", {"name": vr['name'], "version": vr['version']} )
            requests = rsp["requests"] if rsp else []
            vr["_transition_requests"] = requests
        except MlflowReportsException as e:
            print(f"WARNING: Databricks API call failed: {e}")

    data_utils.adjust_ts(vr, [ "creation_timestamp", "last_updated_timestamp" ])
    data_utils.adjust_uc(vr)
    vr[enriched_tags.TAG_REG_MODEL_DOWNLOAD_URI] = get_reg_model_download_uri(vr)
    vr[enriched_tags.TAG_RUN_MODEL_DOWNLOAD_URI] = get_run_model_download_uri(vr)
    link_utils.add_model_version_links(vr)


def _get_mlmodel(registered_model_name, version):
    model_uri = f"models:/{registered_model_name}/{version}"
    mlmodel = get_model_artifact(model_uri, "MLmodel", "yaml")
    explode_utils.explode_json(mlmodel.get("signature"))
    return mlmodel


def _get_vr_run(dct, artifact_max_level):
    vr = dct["model_version"]
    try:
        run_id = vr.get("run_id")
        if run_id:
            dct["run"] = _get_run.get(run_id, artifact_max_level=artifact_max_level)
            experiment_id = dct["run"]["run"]["info"]["experiment_id"]
            dct["experiment"] = get_experiment.get(experiment_id, get_permissions=True)
        else: # NOTE: Some LLM models don't have a run_id. Not documented.
            msg = f'Model version \'{vr["name"]}/{vr["version"]}\' has no run_id'
            dct["run"] = { "warning": msg }
            print(f"WARNING: {msg}")
    except MlflowReportsException as e:
        msg = f'Cannot get run_id \'{run_id}\' for model version \'{vr["name"]}/{vr["version"]}\''
        emsg = exception_utils.to_dict(e, msg)
        print(f"ERROR: {emsg['error']}.")
        dct["run"] = emsg


@click.command()
@opt_registered_model
@opt_model_version
@opt_get_expanded
@opt_artifact_max_level
@opt_get_raw
@opt_silent
@opt_output_file
def main(registered_model, version, artifact_max_level, get_expanded, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(registered_model, version, get_expanded, get_raw, artifact_max_level)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

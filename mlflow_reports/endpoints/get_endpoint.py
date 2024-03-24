"""
Return the JSON API response for a model serving aka "deployment" endpoint.
https://docs.databricks.com/api/workspace/servingendpoints/get
"""

import click
from mlflow_reports.common.click_options import opt_get_raw, opt_silent, opt_output_file
from mlflow_reports.data import data_utils, get_model_version, get_model_signature
from . import get_endpoint_client
from . click_options import opt_endpoint, opt_call_databricks_model_serving, opt_expand_model_version


def get(endpoint_name, call_databricks_model_serving=False, get_raw=False, expand_model_version="none"):
    def _adjust_ts(config, key):
        for x in config.get(key, []):
            data_utils.adjust_ts(x, ["creation_timestamp"])
    client = get_endpoint_client(call_databricks_model_serving)
    rsp = client.get_endpoint(endpoint_name)
    if not get_raw:
        data_utils.adjust_ts(rsp, ["creation_timestamp", "last_updated_timestamp"])
        config = rsp.get("config", {})
        _adjust_ts(config, "served_models")
        _adjust_ts(config, "served_entities")
        if not expand_model_version == "none":
            _enhance_model_version(rsp, expand_model_version)
    return rsp


def _enhance_model_version(rsp, expand_model_version):
    def enhance(e, expand_model_version):
        name =  e["entity_name"]
        version = e["entity_version"]
        get_expanded = expand_model_version == "version-all"
        vr = get_model_version.get(name, version, get_expanded=get_expanded)
        vr = { "entity": e["name"], "model_version": vr }
        if expand_model_version == "version-and-signature":
            sig = get_model_signature.get(f"models:/{name}/{version}")
            vr["signature"] = sig
        return vr
    config = rsp.get("config", {})
    entities = config.get("served_entities", [])
    entities = [ e for e in entities if e.get("entity_version") ]
    if entities:
        rsp["model_versions"] = [ enhance(e, expand_model_version) for e in entities if e.get("entity_version") ]


@click.command()
@opt_endpoint
@opt_call_databricks_model_serving
@opt_get_raw
@opt_output_file
@opt_silent
@opt_expand_model_version
def main(endpoint, call_databricks_model_serving, get_raw, silent, expand_model_version, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(endpoint, call_databricks_model_serving, get_raw, expand_model_version)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

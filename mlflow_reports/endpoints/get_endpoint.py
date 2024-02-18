"""
Return the JSON API response for a model serving aka "deployment" endpoint.
"""

import click
from mlflow_reports.common.click_options import opt_get_raw, opt_silent, opt_output_file
from mlflow_reports.data import data_utils
from . import get_endpoint_client
from . click_options import opt_endpoint, opt_call_databricks_model_serving


def get(endpoint_name, call_databricks_model_serving, get_raw):
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
    return rsp


@click.command()
@opt_endpoint
@opt_call_databricks_model_serving
@opt_get_raw
@opt_output_file
@opt_silent
def main(endpoint, call_databricks_model_serving, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(endpoint, call_databricks_model_serving, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

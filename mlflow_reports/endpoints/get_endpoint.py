"""
Return the JSON response for one endpoint.
"""

import click

from mlflow_reports.data import data_utils
from . import get_endpoint_client
from mlflow_reports.common.click_options import(
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from . click_options import opt_endpoint, opt_call_databricks_model_serving


def get(endpoint_name, call_databricks_model_serving, get_raw):
    client = get_endpoint_client(call_databricks_model_serving)
    rsp = client.get_endpoint(endpoint_name)
    if get_raw:
        return rsp
    data_utils.adjust_ts(rsp, ["creation_timestamp", "last_updated_timestamp"])
    config = rsp.get("config")
    served_models = config.get("served_models")
    for sm in served_models:
        data_utils.adjust_ts(sm, ["creation_timestamp"])
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

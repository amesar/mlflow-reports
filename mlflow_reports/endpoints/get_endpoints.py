import click

from mlflow_reports.data import data_utils
from mlflow_reports.common.click_options import(
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from . click_options import opt_call_databricks_model_serving
from . import get_endpoint_client


def list(call_databricks_model_serving, get_raw):
    client = get_endpoint_client(call_databricks_model_serving)
    endpoints = client.list_endpoints()
    if get_raw:
        return endpoints
    if isinstance(endpoints, dict): # NOTE: Databricks api/2.0/serving-endpoints returns dict and not list
        endpoints = endpoints["endpoints"]
    for ep in endpoints:
        data_utils.adjust_ts(ep, ["creation_timestamp", "last_updated_timestamp"])
    return endpoints


@click.command()
@opt_call_databricks_model_serving
@opt_get_raw
@opt_output_file
@opt_silent
def main(call_databricks_model_serving, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = list(call_databricks_model_serving, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

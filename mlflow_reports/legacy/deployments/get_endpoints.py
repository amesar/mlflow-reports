# https://mlflow.org/docs/latest/llms/deployments/index.html

import os
import click
from mlflow.deployments import get_deploy_client

from mlflow_reports.data import data_utils
from mlflow_reports.common.click_options import(
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from mlflow_reports.model_serving.click_options import opt_get_details
from . import get_endpoint


def list(get_details, get_raw):
    client = get_deploy_client(os.environ.get("MLFLOW_TRACKING_URI"))
    endpoints = client.list_endpoints()
    if get_raw:
        return endpoints
    if get_details:
        return [ get_endpoint.get(ep["name"], get_raw) for ep in endpoints ]
    for ep in endpoints:
        data_utils.adjust_ts(ep, ["creation_timestamp", "last_updated_timestamp"])
    return endpoints

@click.command()
@opt_get_details
@opt_get_raw
@opt_output_file
@opt_silent
def main(get_details, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = list(get_details, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

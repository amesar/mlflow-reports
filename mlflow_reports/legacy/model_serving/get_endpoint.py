import click

from mlflow_reports.client.model_serving_client import ModelServingClient
from mlflow_reports.data import data_utils
from mlflow_reports.common.click_options import(
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from . click_options import opt_endpoint

client = ModelServingClient()


def get(endpoint_name, get_raw):
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
@opt_get_raw
@opt_output_file
@opt_silent
def main(endpoint, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(endpoint, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

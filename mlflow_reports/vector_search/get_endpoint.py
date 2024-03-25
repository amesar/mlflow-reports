# GET /api/2.0/vector-search/endpoints/{endpoint_name}
# https://docs.databricks.com/api/workspace/vectorsearchendpoints/getendpoint

import click

from mlflow_reports.data import data_utils
from mlflow_reports.model_serving.click_options import opt_endpoint
from mlflow_reports.common.click_options import opt_get_raw, opt_silent, opt_output_file
from . import get_VectorSearchClient

client = get_VectorSearchClient()


def get(endpoint_name, get_raw):
    endpoint = client.get_endpoint(endpoint_name)
    if not get_raw:
        data_utils.adjust_ts(endpoint, ["creation_timestamp", "last_updated_timestamp"])
    return endpoint


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

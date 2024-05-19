# GET /api/2.0/vector-search/indexes
# https://docs.databricks.com/api/workspace/vectorsearchindexes/listindexes

import pandas as pd
import click

from mlflow_reports.list import list_utils
from mlflow_reports.common.click_options import opt_output_file_base
from mlflow_reports.list.click_options import opt_columns
from mlflow_reports.model_serving.click_options import opt_endpoint
from mlflow_reports.common import io_utils
from mlflow_reports.common.pandas_utils import move_column
from . import get_VectorSearchClient

client = get_VectorSearchClient()

        
def list_all_indexes():
    endpoints = client.list_endpoints()["endpoints"]
    indexes = [ client.list_indexes(ep["name"]).get("vector_indexes",[]) for ep in endpoints ]
    indexes = [ _idx for _indexes in indexes for _idx in _indexes]
    return endpoints


def list_indexes(endpoint_name):
    return client.list_indexes(endpoint_name)["vector_indexes"]


def show(endpoint_name, columns, output_file_base):
    if endpoint_name:
        indexes = list_indexes(endpoint_name)
    else:
        indexes = list_all_indexes()
    print(f"Found {len(indexes)} for endpoint {endpoint_name}")
    io_utils.write_csv_and_json_files(output_file_base, indexes, columns)


def as_pandas_df(indexes):
    df = pd.DataFrame.from_dict(indexes)
    del df["endpoint_name"]
    move_column(df, "creator", index=1)
    df = df.sort_values(["name"])
    list_utils.to_datetime(df, ["creation_timestamp", "last_updated_timestamp"])
    return df


@click.command()
@opt_endpoint
@opt_columns
@opt_output_file_base
def main(endpoint, columns, output_file_base):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    show(endpoint, columns, output_file_base)


if __name__ == "__main__":
    main()

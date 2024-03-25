# GET  /api/2.0/vector-search/endpoints
# https://docs.databricks.com/api/workspace/vectorsearchendpoints/listendpoints


import click
from mlflow_reports.common.click_options import opt_output_file_base
from mlflow_reports.list.click_options import opt_columns
from mlflow_reports.common import io_utils
from . import get_VectorSearchClient

def list():
    client = get_VectorSearchClient()
    return client.list_endpoints()["endpoints"]

def as_pandas_df(endpoints):
    from mlflow_reports.list import list_utils
    from mlflow_reports.common.pandas_utils import move_column
    import pandas as pd
    df = pd.DataFrame.from_dict(endpoints)
    df = move_column(df, "num_indexes", index=1)
    list_utils.to_datetime(df, ["creation_timestamp", "last_updated_timestamp"])
    return df

def show(columns, output_file_base):
    endpoints = list()
    print(f"Found {len(endpoints)}")
    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(output_file_base, endpoints, columns, ts_columns)


@click.command()
@opt_columns
@opt_output_file_base

def main(columns, output_file_base):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    show(columns, output_file_base)

if __name__ == "__main__":
    main()

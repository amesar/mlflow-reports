"""
List feature tables.
Calls undocumented Databricks endpoint 'api/2.0/feature-store/feature-tables/search'.
"""

from typing import Optional, List
import click

from mlflow_reports.client.http_client import get_mlflow_client
from . import search_feature_tables
from mlflow_reports.list import list_utils
from mlflow_reports.list.click_options import (
    opt_columns,
    opt_output_csv_file,
)

mlflow_client = get_mlflow_client()


def show(columns: List, output_csv_file: Optional[str]):
    df = search_feature_tables.search_as_pandas_df()
    if not df.empty:
        df = df.sort_values(["name"])
    list_utils.show_and_write(df, columns, output_csv_file)
    print(f"Found {df.shape[0]} feature tables")


@click.command()
@opt_columns
@opt_output_csv_file

def main(
        columns,
        output_csv_file
    ):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    if columns:
        columns = columns.split(",")
    show(columns, output_csv_file)


if __name__ == "__main__":
    main()

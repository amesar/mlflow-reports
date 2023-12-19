"""
List all experiments.
"""

import click

from mlflow_reports.client.http_client import get_mlflow_client
from . import search_experiments
from . import list_utils
from . click_options import (
    opt_filter,
    opt_tags_and_aliases_as_string,
    opt_max_results,
    opt_columns,
    opt_max_description,
    opt_output_csv_file,
    opt_view_type,
)

mlflow_client = get_mlflow_client()


def show(filter,
        view_type,
        tags_and_aliases_as_string,
        max_results,
        columns,
        max_description,
        output_csv_file
    ):
    if isinstance(columns, str):
        columns = columns.split(",")
    df = search_experiments.search_as_pandas_df(filter, view_type, max_results, tags_and_aliases_as_string)
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]

    list_utils.show_and_write(df, columns, output_csv_file)
    print(f"Found {df.shape[0]} experiments")


@click.command()
@opt_filter
@opt_view_type
@opt_max_results
@opt_tags_and_aliases_as_string
@opt_columns
@opt_max_description
@opt_output_csv_file

def main(
        filter,
        view_type,
        max_results,
        tags_and_aliases_as_string,
        columns,
        max_description,
        output_csv_file
    ):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    show(**args)


if __name__ == "__main__":
    main()

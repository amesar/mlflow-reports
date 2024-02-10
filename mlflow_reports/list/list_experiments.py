"""
List all experiments.
"""

import click

from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from . click_options import (
    opt_filter,
    opt_tags_and_aliases_as_string,
    opt_max_results,
    opt_columns,
    opt_max_description,
    opt_view_type,
)
from . import search_experiments

mlflow_client = get_mlflow_client()


def show(filter,
        view_type,
        tags_and_aliases_as_string,
        max_results,
        columns,
        max_description,
        output_file_base
    ):
    if isinstance(columns, str):
        columns = columns.split(",")
    experiments = search_experiments.search(filter, view_type, max_results, tags_and_aliases_as_string)
    df = search_experiments.to_pandas_df(experiments)
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]
    ts_columns = [ "creation_time", "last_update_time" ]
    experiments = search_experiments.search(filter, view_type, max_results, tags_and_aliases_as_string)
    io_utils.write_csv_and_json_files(output_file_base, experiments, columns, ts_columns)
    print(f"Found {len(experiments)} experiments")


@click.command()
@opt_filter
@opt_view_type
@opt_max_results
@opt_tags_and_aliases_as_string
@opt_columns
@opt_max_description
@opt_output_file_base

def main(
        filter,
        view_type,
        max_results,
        tags_and_aliases_as_string,
        columns,
        max_description,
        output_file_base
    ):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    show(**args)


if __name__ == "__main__":
    main()

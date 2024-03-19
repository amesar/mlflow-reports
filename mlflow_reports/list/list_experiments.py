"""
List all experiments.
"""

import click

from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from . click_options import (
    opt_filter,
    opt_max_results,
    opt_columns,
    opt_view_type,
)
from . import search_experiments


def show(filter,
        view_type,
        max_results,
        columns,
        output_file_base
    ):
    if isinstance(columns, str):
        columns = columns.split(",")
    experiments = search_experiments.search(filter, view_type, max_results)
    ts_columns = [ "creation_time", "last_update_time" ]
    io_utils.write_csv_and_json_files(output_file_base, experiments, columns, ts_columns)
    print(f"Found {len(experiments)} experiments")


@click.command()
@opt_filter
@opt_view_type
@opt_max_results
@opt_columns
@opt_output_file_base

def main(
        filter,
        view_type,
        max_results,
        columns,
        output_file_base
    ):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    show(**args)


if __name__ == "__main__":
    main()

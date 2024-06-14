"""
List all registered models.
"""

import click
from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from . import search_registered_models
from . click_options import (
    opt_filter,
    opt_prefix,
    opt_get_tags_and_aliases,
    opt_unity_catalog,
    opt_columns,
)


def show(filter,
        prefix,
        get_tags_and_aliases,
        unity_catalog,
        columns,
        output_file_base
    ):
    if isinstance(columns, str):
        columns = columns.split(",")
    models = search_registered_models.search(filter, prefix, get_tags_and_aliases, unity_catalog)
    print(f"Found {len(models)} registered models")

    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(output_file_base, models, columns, ts_columns)
    print(f"Found {len(models)} registered models")


@click.command()
@opt_filter
@opt_get_tags_and_aliases
@opt_unity_catalog
@opt_prefix
@opt_columns
@opt_output_file_base

def main(
        filter,
        prefix,
        get_tags_and_aliases,
        unity_catalog,
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

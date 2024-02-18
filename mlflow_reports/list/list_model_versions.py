"""
List model versions.
"""

import click
from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from . import search_model_versions
from . click_options import (
    opt_filter,
    opt_get_tags_and_aliases,
    opt_get_model_details,
    opt_unity_catalog,
    opt_columns,
    opt_max_description
)


def show(filter,
        get_tags_and_aliases,
        get_model_details,
        unity_catalog,
        columns,
        max_description,
        output_file_base
    ):
    versions = search_model_versions.search(
        filter = filter,
        get_tags_and_aliases = get_tags_and_aliases,
        get_model_details = get_model_details,
        unity_catalog = unity_catalog
    )
    df = search_model_versions.to_pandas_df(versions)
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]

    if not df.empty:
        df = df.sort_values(["name", "version"], ascending=[True, False])
    io_utils.write_csv_and_json_files(output_file_base, versions, columns)


@click.command()
@opt_filter
@opt_get_tags_and_aliases
@opt_get_model_details
@opt_unity_catalog
@opt_columns
@opt_max_description
@opt_output_file_base

def main(
        filter,
        get_tags_and_aliases,
        get_model_details,
        unity_catalog,
        columns,
        max_description,
        output_file_base
    ):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    if columns:
        args["columns"] = columns.split(",")
    show(**args)


if __name__ == "__main__":
    main()

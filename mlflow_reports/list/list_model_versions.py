"""
List model versions.
"""

import click

from mlflow_reports.client.http_client import get_mlflow_client
from . import search_model_versions
from . import list_utils
from . click_options import (
    opt_filter,
    opt_get_tags_and_aliases,
    opt_tags_and_aliases_as_string,
    opt_get_model_details,
    opt_get_search_object_again,
    opt_unity_catalog,
    opt_columns,
    opt_max_description,
    opt_output_csv_file,
)

mlflow_client = get_mlflow_client()


def show(filter,
        get_tags_and_aliases,
        tags_and_aliases_as_string,
        get_model_details,
        get_search_object_again,
        unity_catalog,
        columns,
        max_description,
        output_csv_file
    ):
    df = search_model_versions.search(
        filter = filter,
        get_tags_and_aliases = get_tags_and_aliases,
        tags_and_aliases_as_string = tags_and_aliases_as_string,
        get_model_details = get_model_details,
        get_search_object_again = get_search_object_again,
        unity_catalog = unity_catalog
    )
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]

    if not df.empty:
        df = df.sort_values(["name", "version"], ascending=[True, False])
    list_utils.show_and_write(df, columns, output_csv_file)
    print(f"Found {df.shape[0]} model versions")


@click.command()
@opt_filter
@opt_get_tags_and_aliases
@opt_tags_and_aliases_as_string
@opt_get_model_details
@opt_get_search_object_again
@opt_unity_catalog
@opt_columns
@opt_max_description
@opt_output_csv_file

def main(
        filter,
        get_tags_and_aliases,
        tags_and_aliases_as_string,
        get_model_details,
        get_search_object_again,
        unity_catalog,
        columns,
        max_description,
        output_csv_file
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

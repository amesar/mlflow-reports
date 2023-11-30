"""
List all registered models.
"""

import click
from mlflow_reports.client.http_client import get_mlflow_client
from . import search_registered_models
from . import list_utils
from . click_options import (
    opt_filter,
    opt_prefix,
    opt_get_tags_and_aliases,
    opt_unity_catalog,
    opt_columns,
    opt_max_description,
    opt_output_csv_file,
)

mlflow_client = get_mlflow_client()


def show(filter,
        prefix,
        get_tags_and_aliases,
        unity_catalog,
        columns,
        max_description,
        output_csv_file
    ):
    if isinstance(columns, str):
        columns = columns.split(",")
    df = search_registered_models.search_as_pandas_df(filter, prefix, get_tags_and_aliases, unity_catalog)
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]

    list_utils.show_and_write(df, columns, output_csv_file)
    print(f"Found {df.shape[0]} registered models")


@click.command()
@opt_filter
@opt_get_tags_and_aliases
@opt_unity_catalog
@opt_prefix
@opt_columns
@opt_max_description
@opt_output_csv_file

def main(
        filter,
        prefix,
        get_tags_and_aliases,
        unity_catalog,
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

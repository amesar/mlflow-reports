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
    opt_tags_and_aliases_as_string,
    opt_unity_catalog,
    opt_columns,
    opt_max_description,
    opt_output_csv_file,
)

mlflow_client = get_mlflow_client()


def show(filter,
        prefix,
        get_tags_and_aliases,
        tags_and_aliases_as_string,
        unity_catalog,
        columns,
        max_description,
        output_csv_file
    ):
    df = search_registered_models.search(filter, prefix, get_tags_and_aliases, tags_and_aliases_as_string, unity_catalog)
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]

    list_utils.show_and_write(df, columns, output_csv_file)


@click.command()
@opt_filter
@opt_get_tags_and_aliases
@opt_tags_and_aliases_as_string
@opt_unity_catalog
@opt_prefix
@opt_columns
@opt_max_description
@opt_output_csv_file

def main(
        filter, 
        prefix, 
        get_tags_and_aliases, 
        tags_and_aliases_as_string, 
        unity_catalog, 
        columns, 
        max_description, 
        output_csv_file
    ):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    #if columns:
        #args["columns"] = columns.split(",")
    show(**args)

    #print("Options:")
    #for k,v in locals().items():
        #print(f"  {k}: {v}")
    #show(filter, prefix, get_tags_and_aliases, tags_and_aliases_as_string, unity_catalog, max_description, output_csv_file)

if __name__ == "__main__":
    main()

"""
List model versions.
"""

import click
from mlflow_reports.client.http_client import get_mlflow_client


from . import list_utils
from . click_options import (
    opt_filter, 
    opt_get_tags_and_aliases,
    opt_tags_and_aliases_as_string,
    opt_unity_catalog,
    opt_max_description, 
    opt_output_csv_file,
)
from . import search_api


mlflow_client = get_mlflow_client()

def show(filter,
        get_tags_and_aliases,
        tags_and_aliases_as_string,
        unity_catalog,
        max_description,
        output_csv_file
    ):
    df = search_api.search_model_versions(
        filter = filter,
        get_tags_and_aliases = get_tags_and_aliases,
        tags_and_aliases_as_string = tags_and_aliases_as_string,
        unity_catalog = unity_catalog
    )
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]
    list_utils.show_and_write(df, output_csv_file)


@click.command()
@opt_filter
@opt_get_tags_and_aliases
@opt_tags_and_aliases_as_string
@opt_unity_catalog
@opt_max_description
@opt_output_csv_file

def main(filter, get_tags_and_aliases, tags_and_aliases_as_string, unity_catalog, max_description, output_csv_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    show(filter, get_tags_and_aliases, tags_and_aliases_as_string, unity_catalog, max_description, output_csv_file)


if __name__ == "__main__":
    main()

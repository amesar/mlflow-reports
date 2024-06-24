"""
List UC registered models.
"""

import click
from mlflow_reports.client import unity_catalog_client
from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from . click_options import opt_columns, opt_max_results, opt_catalog, opt_schema


@click.command()
@opt_catalog
@opt_schema
@opt_columns
@opt_max_results
@opt_output_file_base

def main(catalog, schema, columns, max_results, output_file_base):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    models = unity_catalog_client.list_registered_models(catalog, schema, max_results)
    models = sorted(models, key=lambda x: x["full_name"])
    io_utils.write_csv_and_json_files(output_file_base, models, columns, ["created_at", "updated_at" ])


if __name__ == "__main__":
    main()

"""
Get table lineage from Databricks REST API.

* Not documented in Databricks REST API docs
* But example exists in:  https://docs.databricks.com/data-governance/unity-catalog/data-lineage.html#retrieve-table-lineage
"""

from typing import Dict
import click

from mlflow_reports.client import databricks_client
from mlflow_reports.data import data_utils
from mlflow_reports.common.click_options import opt_table, opt_silent, opt_output_file


def get(table_name: str) -> Dict:
    return databricks_client.get_table_lineage(table_name)


@click.command()
@opt_table
@opt_output_file
@opt_silent
def main(table, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(table)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

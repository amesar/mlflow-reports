"""
Get API JSON response for a Unity Catalog table.
Call Databricks endpoint 'api/2.1/unity-catalog/tables/${table_name}'
"""

from typing import Optional, Dict
import click

from mlflow_reports.client.http_client import HttpClient
from mlflow_reports.common import explode_utils
from mlflow_reports.data import data_utils
from mlflow_reports.common.click_options import(
    opt_table,
    opt_get_raw,
    opt_silent,
    opt_output_file
)

client = HttpClient("api/2.1")


def get(table_name: str, get_raw: Optional[bool] = False) -> Dict:
    table = client.get(f"unity-catalog/tables/{table_name}")
    if not get_raw:
        data_utils.adjust_ts(table, ["created_at", "updated_at"])
        explode_utils.explode_json(table.get("columns"))
    return table


@click.command()
@opt_table
@opt_get_raw
@opt_output_file
@opt_silent
def main(table, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(table, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

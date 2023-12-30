"""
Get API JSON response for one feature table.
Call undocumented Databricks endpoint 'api/2.0/feature-store/feature-tables/get/{table_name}'.
"""

from typing import Optional, Dict
import click

from mlflow_reports.client.feature_store_client import FeatureStoreClient
from mlflow_reports.data import data_utils
from mlflow_reports.common.click_options import(
    opt_get_raw,
    opt_silent,
    opt_output_file
)
from . click_options import opt_table, opt_get_from_search

client = FeatureStoreClient()


def get(table_name: str, get_from_search: Optional[bool] = False, get_raw: Optional[bool] = False) -> Dict:
    rsp = client.get_table(table_name, get_from_search)
    if get_raw:
        return rsp
    table = rsp.get("feature_table")
    if table:
        data_utils.adjust_ts(table, ["creation_timestamp", "last_updated_timestamp"])
        for nbp in table.get("notebook_producers", []):
            data_utils.adjust_ts(nbp, ["creation_timestamp"])
    return rsp


@click.command()
@opt_table
@opt_get_from_search
@opt_get_raw
@opt_output_file
@opt_silent
def main(table, get_from_search, get_raw, silent, output_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = get(table, get_from_search, get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

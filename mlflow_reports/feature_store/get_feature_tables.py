"""
Get API JSON response for all feature tables.
Call undocumented Databricks endpoint 'api/2.0/feature-store/feature-tables/search'.
"""

from typing import Optional, List
import click

from mlflow_reports.client.feature_store_client import FeatureStoreClient
from mlflow_reports.data import data_utils
from mlflow_reports.common.click_options import(
    opt_get_raw,
    opt_silent,
    opt_output_file
)

client = FeatureStoreClient()

def list(get_raw: bool = False) -> List:
    tables = client.search()
    if get_raw:
        return tables
    tables = sorted(tables, key=lambda tbl: tbl["name"])
    for tbl in tables:
        data_utils.adjust_ts(tbl, ["creation_timestamp", "last_updated_timestamp"])
        for nbp in tbl.get("notebook_producers", []):
            data_utils.adjust_ts(nbp, ["creation_timestamp"])
    return tables

@click.command()
@opt_get_raw
@opt_output_file
@opt_silent
#def main(summary_view, get_details, get_raw, silent, output_file):
def main(get_raw: bool, silent: bool, output_file: str):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    dct = list(get_raw)
    data_utils.dump_object(dct, output_file, silent)


if __name__ == "__main__":
    main()

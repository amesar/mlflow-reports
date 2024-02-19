"""
Create and show a Pandas dataframe and text table from the JSON response for endpoints entities.
"""

import click

from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from mlflow_reports.list.click_options import opt_columns, opt_normalize_pandas_df
from . click_options import opt_call_databricks_model_serving
from . import get_endpoints


def show(columns, output_file_base, call_databricks_model_serving=False, normalize_pandas_df=False):
    def reorder_columns(df, column):
        if column in df:
            columns = list(df.columns)
            columns.remove(column)
            columns.insert(1, column)
            df = df[columns]
        return df
    def mv_endpoint_type_column(df):
        return reorder_columns(df, "endpoint_type")
    def mv_ep_endpoint_type_column(df):
        return reorder_columns(df, "ep_endpoint_type")
    endpoints = get_endpoints(call_databricks_model_serving)

    # write endpoints
    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(f"{output_file_base}", endpoints, columns, ts_columns, normalize_pandas_df, mv_endpoint_type_column)

    # write endpoint entities
    ts_columns = [ "ep_creation_timestamp", "ep_last_updated_timestamp" ]
    entities = list_entities(endpoints)
    base = f"{output_file_base}_entities"
    io_utils.write_csv_and_json_files(base, entities, columns, ts_columns, normalize_pandas_df, mv_ep_endpoint_type_column)

    # write endpoints without entities, not READY state
    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    endpoints = list_endpoints_without_entities(endpoints)
    base = f"{output_file_base}_without_entities"
    io_utils.write_csv_and_json_files(base, endpoints, [], ts_columns, normalize_pandas_df)


def list_entities(endpoints):
    def mk_entities(ep):
        config = ep.get("config", {})
        served_entities = config.get("served_entities", [])
        return [ { **_mk_ep(ep),  **ent} for ent in served_entities ]
    return _mk_entities(endpoints, mk_entities)


def list_endpoints_without_entities(endpoints):
    return [ ep for ep in endpoints if not ep.get("config") ]

def _mk_entities(endpoints, func):
    return [ent for ep in endpoints for ent in func(ep)]

def _rename_endpoint_keys(dct, keys, prefix):
    def rename(k, prefix):
        return f"{prefix}_{k}"
    return { rename(k,prefix):v for k,v in dct.items() if k in keys }

def _mk_ep(ep):
    keys = ["name", "endpoint_type", "creator", "creation_timestamp", "last_updated_timestamp", "state" ]
    return _rename_endpoint_keys(ep, keys, "ep")


@click.command()
@opt_columns
@opt_output_file_base
@opt_call_databricks_model_serving
@opt_normalize_pandas_df
def main(columns, output_file_base, call_databricks_model_serving, normalize_pandas_df):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    show(columns, output_file_base, call_databricks_model_serving, normalize_pandas_df)


if __name__ == "__main__":
    main()

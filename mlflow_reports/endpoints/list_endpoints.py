"""
Create and show a Pandas dataframe and text table from the JSON response for all endpoints.
"""

import click
from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base, opt_get_raw, opt_get_details
from mlflow_reports.list.click_options import opt_columns, opt_normalize_pandas_df
from . click_options import opt_call_databricks_model_serving, opt_model_type
from . import get_endpoints, get_endpoint_client, as_pandas_df


def show(
        model_type,
        columns,
        output_file_base,
        call_databricks_model_serving = False,
        get_raw = False,
        get_details = False,
        normalize_pandas_df = False
    ):
    endpoints = get_endpoints(model_type, call_databricks_model_serving)
    if get_details: # NOTE: "GET serving-endpoints/{endpoint_name}" returns more details than "GET serving-endpoints"
        client = get_endpoint_client(call_databricks_model_serving)
        endpoints = [ client.get_endpoint(ep["name"]) for ep in endpoints ]
    ts_columns = [] if get_raw else [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(output_file_base, endpoints, columns, ts_columns, normalize_pandas_df)

    df = as_pandas_df(endpoints)
    io_utils.write_csv_and_json_files(endpoints, df, columns, output_file_base+"2")


@click.command()
@opt_model_type
@opt_columns
@opt_output_file_base
@opt_call_databricks_model_serving
@opt_get_raw
@opt_get_details
@opt_normalize_pandas_df
def main(
        model_type,
        columns,
        output_file_base,
        call_databricks_model_serving,
        get_raw = False,
        get_details = False,
        normalize_pandas_df = False
    ):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    show(model_type, columns, output_file_base, call_databricks_model_serving, get_raw, get_details, normalize_pandas_df)


if __name__ == "__main__":
    main()

import click
import pandas as pd

from mlflow_reports.list.click_options import opt_columns, opt_output_csv_file
from mlflow_reports.list import list_utils
from . click_options import opt_call_databricks_model_serving
from . import get_endpoint_client


def create_pandas_df(call_databricks_model_serving=False):
    client = get_endpoint_client(call_databricks_model_serving)
    endpoints = client.list_endpoints()
    if isinstance(endpoints, dict): # NOTE: Databricks api/2.0/serving-endpoints returns dict and not list
        endpoints = endpoints["endpoints"]
    df = pd.json_normalize(endpoints)
    list_utils.to_datetime(df, "creation_timestamp")
    list_utils.to_datetime(df, "last_updated_timestamp")
    return df

@click.command()
@opt_columns
@opt_output_csv_file
@opt_call_databricks_model_serving
def main(columns, output_csv_file, call_databricks_model_serving):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    df = create_pandas_df(call_databricks_model_serving)
    print(f"Found {df.shape[0]} routes")
    if isinstance(columns, str):
        columns = columns.split(",")
    list_utils.show_and_write(df, columns, output_csv_file)

if __name__ == "__main__":
    main()

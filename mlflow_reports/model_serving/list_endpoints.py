import click
import pandas as pd

from mlflow_reports.client.model_serving_client import ModelServingClient
from mlflow_reports.list.click_options import opt_columns, opt_output_csv_file
from mlflow_reports.list import list_utils

client = ModelServingClient()

def create_pandas_df():
    endpoints = client.list_endpoints()
    endpoints = endpoints["endpoints"]
    df = pd.json_normalize(endpoints)
    list_utils.to_datetime(df, "creation_timestamp")
    list_utils.to_datetime(df, "last_updated_timestamp")
    return df

@click.command()
@opt_columns
@opt_output_csv_file
def main(columns, output_csv_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    df = create_pandas_df()
    print(f"Found {df.shape[0]} routes")
    if isinstance(columns, str):
        columns = columns.split(",")
    list_utils.show_and_write(df, columns, output_csv_file)

if __name__ == "__main__":
    main()

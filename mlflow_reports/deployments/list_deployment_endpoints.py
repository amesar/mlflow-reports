# * https://mlflow.org/docs/latest/llms/deployments/index.html

import os
import pandas as pd
import click
from mlflow.deployments import get_deploy_client
from mlflow_reports.list.click_options import opt_columns, opt_output_csv_file
from mlflow_reports.list import list_utils


def list():
    client = get_deploy_client(os.environ.get("MLFLOW_TRACKING_URI"))
    endpoints = client.list_endpoints()
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
    df = list()
    print(f"Found {df.shape[0]} routes")
    if isinstance(columns, str):
        columns = columns.split(",")
    list_utils.show_and_write(df, columns, output_csv_file)


if __name__ == "__main__":
    main()

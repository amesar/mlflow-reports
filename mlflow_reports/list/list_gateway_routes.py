# https://mlflow.org/docs/latest/python_api/mlflow.gateway.html

import pandas as pd
import click
import mlflow
from . click_options import opt_columns, opt_output_csv_file
from . import list_utils

print("gateway_uri:", mlflow.gateway.get_gateway_uri())


def list_routes():
    routes = mlflow.gateway.search_routes()
    data = [ (rt.name, rt.route_type, rt.model.name, rt.model.provider) for rt in routes ]
    df =  pd.DataFrame(data, columns = ["name", "route_type", "model_name", "model_provider"])
    df = df.sort_values(["name", "route_type"])
    return df


@click.command()
@opt_columns
@opt_output_csv_file

def main(columns, output_csv_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    df = list_routes()
    print(f"Found {df.shape[0]} routes")
    if isinstance(columns, str):
        columns = columns.split(",")
    list_utils.show_and_write(df, columns, output_csv_file)


if __name__ == "__main__":
    main()

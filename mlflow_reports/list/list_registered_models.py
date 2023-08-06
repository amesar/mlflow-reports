"""
List all registered models.
"""

import click
from mlflow_reports.client.http_client import get_mlflow_client
from . click_options import opt_max_description, opt_output_csv_file, opt_filter, opt_prefix
from . import search_api
from tabulate import tabulate

mlflow_client = get_mlflow_client()


def show(filter, prefix, max_description, output_csv_file):
    df = search_api.search_registered_models(filter, prefix, max_description)
    #df = as_pandas_df(filter, prefix, max_description)
    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
    if output_csv_file:
        with open(output_csv_file, "w", encoding="utf-8") as f:
            df.to_csv(f, index=False)


@click.command()
@opt_max_description
@opt_output_csv_file 
@opt_prefix
@opt_filter
def main(max_description, filter, prefix, output_csv_file):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    show(filter, prefix, max_description, output_csv_file)

if __name__ == "__main__":
    main()

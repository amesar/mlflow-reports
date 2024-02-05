import click
from mlflow_reports.common.click_options import opt_output_file_base
from mlflow_reports.list.click_options import opt_columns
from mlflow_reports.common import io_utils
from . import get_VectorSearchClient

client = get_VectorSearchClient()


def list_endpoints(columns, output_file_base):
    endpoints = client.list_endpoints()["endpoints"]
    print(f"Found {len(endpoints)}")
    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(output_file_base, endpoints, columns, ts_columns)


@click.command()
@opt_columns
@opt_output_file_base

def main(columns, output_file_base):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    list_endpoints(columns, output_file_base)

if __name__ == "__main__":
    main()

"""
Create and show a Pandas dataframe and text table from the JSON response for all endpoints.
"""

import click
from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base, opt_get_raw, opt_get_details
from mlflow_reports.list.click_options import opt_columns, opt_normalize_pandas_df
from . click_options import opt_use_deployment_client, opt_model_type
from . import get_endpoints, get_endpoint_client, get_openapi_schema


def show(
        model_type,
        openapi,
        columns,
        output_file_base,
        use_deployment_client = False,
        get_raw = False,
        get_details = False,
        normalize_pandas_df = False
    ):
    endpoints = get_endpoints(model_type, use_deployment_client)
    client = get_endpoint_client(use_deployment_client)
    if get_details: # NOTE: "GET serving-endpoints/{endpoint_name}" returns more details than "GET serving-endpoints"
        endpoints = [ client.get_endpoint(ep["name"]) for ep in endpoints ]
    ts_columns = [] if get_raw else [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(output_file_base, endpoints, columns, ts_columns, normalize_pandas_df, silent=True)
    if openapi:
        import json
        openapi_schemas = _get_endpoint_openapi_schemas(client, endpoints)
        path = f"{output_file_base}_openapi.json"
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(openapi_schemas, indent=2)+"\n")


def _get_endpoint_openapi_schemas(client, endpoints):
    def _get_openapi_schema(client, endpoint_name):
        rsp = get_openapi_schema(client, endpoint_name)
        return { "endpoint": endpoint_name, "openapi": rsp }
    return [ _get_openapi_schema(client, ep["name"]) for ep in endpoints ]


@click.command()
@opt_model_type
@click.option("--openapi",
    help="Write OpenAPI schema for all endpoints to file '{output-file-base}_opena[i.json'.",
    type=bool,
    default=False)
@opt_columns
@opt_output_file_base
@opt_use_deployment_client
@opt_get_raw
@opt_get_details
@opt_normalize_pandas_df
def main(
        model_type,
        openapi,
        columns,
        output_file_base,
        use_deployment_client,
        get_raw = False,
        get_details = False,
        normalize_pandas_df = False
    ):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    if isinstance(columns, str):
        columns = columns.split(",")
    show(model_type, openapi, columns, output_file_base, use_deployment_client, get_raw, get_details, normalize_pandas_df)


if __name__ == "__main__":
    main()

"""
List model versions.
"""

import click
from mlflow_reports.common import io_utils
from mlflow_reports.common.click_options import opt_output_file_base
from . import search_model_versions
from . click_options import (
    opt_filter,
    opt_prefix,
    opt_get_tags_and_aliases,
    opt_get_model_details,
    opt_unity_catalog,
    opt_columns
)


def show(filter,
        prefix,
        get_tags_and_aliases,
        get_model_details,
        unity_catalog,
        columns,
        output_file_base
    ):
    versions = search_model_versions.search(
        filter = filter,
        prefix = prefix,
        get_tags_and_aliases = get_tags_and_aliases,
        get_model_details = get_model_details,
        unity_catalog = unity_catalog
    )
    total_size = _calc_total_size(versions)
    _to_commas(versions)
    ts_columns = [ "creation_timestamp", "last_updated_timestamp" ]
    io_utils.write_csv_and_json_files(output_file_base, versions, columns, ts_columns)
    print(f"Found {len(versions)} model versions")
    print(f"Total bytes: {total_size:,} bytes")
    GB = 1000 * 1000000
    if total_size > GB:
        total_size = round((total_size/GB),3)
        print(f"Total bytes: {total_size:,} GB")

def _to_commas(versions):
    for vr in versions:
        size = vr.get("model_size")
        if size and isinstance(size,int):
            vr["model_size"] = f"{size:,}"

def _calc_total_size(versions):
    def _get_model_size(vr):
        return vr.get("model_size",0) or 0
    if len(versions)==0:
        return 0
    total_size = sum([_get_model_size(vr) for vr in versions])
    return total_size


@click.command()
@opt_filter
@opt_prefix
@opt_get_tags_and_aliases
@opt_get_model_details
@opt_unity_catalog
@opt_columns
@opt_output_file_base

def main(
        filter,
        prefix,
        get_tags_and_aliases,
        get_model_details,
        unity_catalog,
        columns,
        output_file_base
    ):
    print("Options:")
    args = locals()
    for k,v in args.items():
        print(f"  {k}: {v}")
    if columns:
        args["columns"] = columns.split(",")
    show(**args)


if __name__ == "__main__":
    main()

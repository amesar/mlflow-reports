import pandas as pd
from tabulate import tabulate

from mlflow_reports.common.timestamp_utils import TS_FORMAT
from mlflow_reports.common import object_utils


def to_datetime(df, column_or_columns, datetime_as_string=False):
    if isinstance(column_or_columns, list):
        for column in column_or_columns:
            _to_datetime(df, column, datetime_as_string)
    else: # expecting string
        _to_datetime(df, column_or_columns, datetime_as_string)


def _to_datetime(df, column, datetime_as_string=False):
    df[column] = pd.to_datetime(df[column]/1000, unit="s").dt.round("1s")
    if datetime_as_string:
        df[column] = df[column].dt.strftime(TS_FORMAT)


def show_and_write(df, columns=None, csv_file=None):
    """
    Display Pandas dataframe to stdout and writes to file.
    """
    if df.empty:
        print(f"WARNING: no search results")
        return

    if columns:
        columns = [c for c in columns if c in df.columns ]
        df = df[columns]

    print(tabulate(df, headers="keys", tablefmt="psql", numalign="right", showindex=False))
    if csv_file:
        with open(csv_file, "w", encoding="utf-8") as f:
            df.to_csv(f, index=False)


def kv_list_to_dict(model_or_version, key, func, tags_and_aliases_as_string):
    """
    Convert a tag k/v list or alias k/v list to a dict.
    """
    kv_list = model_or_version.get(key)
    if kv_list:
        model_or_version[key] = func(kv_list)
        dct = func(kv_list)
        if tags_and_aliases_as_string:
            dct = object_utils.dict_to_json(dct)
        model_or_version[key] = dct

import pandas as pd
from mlflow_reports.common.timestamp_utils import TS_FORMAT


def to_datetime(df, column, datetime_as_string=False):
    df[column] = pd.to_datetime(df[column]/1000, unit="s").dt.round("1s")
    if datetime_as_string:
        df[column] = df[column].dt.strftime(TS_FORMAT)

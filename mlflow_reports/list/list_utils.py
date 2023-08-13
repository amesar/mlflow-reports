import pandas as pd
from tabulate import tabulate
from mlflow_reports.common.timestamp_utils import TS_FORMAT


def to_datetime(df, column, datetime_as_string=False):
    df[column] = pd.to_datetime(df[column]/1000, unit="s").dt.round("1s")
    if datetime_as_string:
        df[column] = df[column].dt.strftime(TS_FORMAT)


def show_and_write(df, output_csv_file):
    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
    if output_csv_file:
        with open(output_csv_file, "w", encoding="utf-8") as f:
            df.to_csv(f, index=False)

import pandas as pd
from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.timestamp_utils import TS_FORMAT

mlflow_client = get_mlflow_client()


def search_registered_models(filter=None, prefix=None):
    models = SearchRegisteredModelsIterator(mlflow_client, filter=filter)
    models = list(models)
    if prefix:
        models = [ m for m in models if m["name"].startswith(prefix)]
    models = sorted(models, key=lambda x: x["name"])
    print(f"Found {len(models)} registered models")
    return models


def to_datetime(df, column, datetime_as_string=False):
    df[column] = pd.to_datetime(df[column]/1000, unit="s").dt.round("1s")
    if datetime_as_string:
        df[column] = df[column].dt.strftime(TS_FORMAT)

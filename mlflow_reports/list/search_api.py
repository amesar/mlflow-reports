"""
List objects
"""

import pandas as pd
import numpy as np
from . import list_utils

from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator
from mlflow_reports.client.http_client import get_mlflow_client
mlflow_client = get_mlflow_client()

def search_registered_models(filter=None, prefix=None, datetime_as_string=False, max_description=None):
    models = SearchRegisteredModelsIterator(mlflow_client, filter=filter)
    models = list(models)
    if prefix:
        models = [ m for m in models if m["name"].startswith(prefix)]
    models = sorted(models, key=lambda x: x["name"])
    print(f"Found {len(models)} registered models")

    columns = ["name", "user_id", "creation_timestamp", "last_updated_timestamp" ]
    if len(models) == 0:
        return pd.DataFrame(columns=columns)

    df = pd.DataFrame.from_dict(models)
    if not "user_id" in df:
        columns.remove("user_id")

    if "description" in df:
        columns.append("description")

    df = df.replace(np.nan, "", regex=True)
    df = df[columns] 
    list_utils.to_datetime(df, "creation_timestamp", datetime_as_string)
    list_utils.to_datetime(df, "last_updated_timestamp", datetime_as_string)

    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]
    return df

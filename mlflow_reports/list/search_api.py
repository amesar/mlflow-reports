"""
List objects
"""

import pandas as pd
import numpy as np
from . import list_utils

from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator
from mlflow_reports.common import mlflow_utils, object_utils


def search_registered_models(filter=None, 
        prefix = None, 
        datetime_as_string = False, 
        get_tags_and_aliases = False, 
        tags_and_aliases_as_string = False, 
        unity_catalog = False
    ):
    if unity_catalog:
        mlflow_utils.use_unity_catalog()
    mlflow_client = get_mlflow_client()
    models = SearchRegisteredModelsIterator(mlflow_client, filter=filter)
    models = list(models)
    if prefix:
        models = [ m for m in models if m["name"].startswith(prefix)]
    models = sorted(models, key=lambda x: x["name"])
    print(f"Found {len(models)} registered models")

    for model in models:
        _to_dict(model, "tags", mlflow_utils.mk_tags_dict, tags_and_aliases_as_string)
        _to_dict(model, "aliases", mlflow_utils.mk_aliases_dict, tags_and_aliases_as_string)

    columns = ["name", "user_id", "creation_timestamp", "last_updated_timestamp" ]
    if get_tags_and_aliases:
        columns += [ "tags", "aliases" ]

    if len(models) == 0:
        return pd.DataFrame(columns=columns)

    df = pd.DataFrame.from_dict(models)
    if not "user_id" in df:
        columns.remove("user_id")
    if get_tags_and_aliases:
        if not "tags" in df:
            columns.remove("tags")
        if not "aliases" in df:
            columns.remove("aliases")

    if "description" in df:
        columns.append("description")
    df = df.replace(np.nan, "", regex=True)
    df = df[columns] 
    list_utils.to_datetime(df, "creation_timestamp", datetime_as_string)
    list_utils.to_datetime(df, "last_updated_timestamp", datetime_as_string)

    return df


def _to_dict(model, key, func, tags_and_aliases_as_string):
    kv_list = model.get(key)
    if kv_list:
        model[key] = func(kv_list)
        dct = func(kv_list)
        if tags_and_aliases_as_string:
            dct = object_utils.dict_to_json(dct)
        model[key] = dct

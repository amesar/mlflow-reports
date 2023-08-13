"""
Search for registered models and model version and returns Pandas DataFrame
"""

import mlflow
import pandas as pd
import numpy as np
from . import list_utils

from mlflow_reports.data import get_mlflow_model
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator, SearchModelVersionsIterator
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

    return df


def search_model_versions(filter=None, 
        get_tags_and_aliases = False, 
        tags_and_aliases_as_string = False, 
        unity_catalog = False
    ):
    if unity_catalog:
        mlflow_utils.use_unity_catalog()
    mlflow_client = get_mlflow_client()
    if mlflow_utils.is_calling_databricks():
        versions = _list_model_versions_databricks(mlflow_client, filter, get_tags_and_aliases)
    else:
        versions = _list_model_versions_open_source(mlflow_client, filter, get_tags_and_aliases)
    if tags_and_aliases_as_string:
        for vr in versions:
            _to_dict(vr, "tags", mlflow_utils.mk_tags_dict, True)
    df = pd.DataFrame.from_dict(versions)
    list_utils.to_datetime(df, "creation_timestamp")
    list_utils.to_datetime(df, "last_updated_timestamp")
    return df


def _list_model_versions_open_source(mlflow_client, filter, get_tags_and_aliases):
    versions = _list_versions(mlflow_client, filter, get_tags_and_aliases)
    return versions

def _list_model_versions_databricks(mlflow_client, filter, get_tags_and_aliases):
    if filter:
        return _list_model_versions_open_source(mlflow_client, filter, get_tags_and_aliases)
    models = SearchRegisteredModelsIterator(mlflow_client)
    models = list(models)    
    num_models = len(models)    
    print(f"Found {num_models} models")
    versions = []
    for j, model in enumerate(models):
        print(f"Processing {j+1}/{num_models} model '{model['name']}'")
        filter = f"name='{model['name']}'"
        vrs = _list_versions(mlflow_client, filter, get_tags_and_aliases)
        if vrs:
            versions += vrs
    print(f"Found {len(versions)} model versions")
    return versions

def _list_versions(mlflow_client, filter, get_tags_and_aliases):
    versions = SearchModelVersionsIterator(mlflow_client, filter=filter)
    versions = list(versions)
    if len(versions) == 0:
        print(f"WARNING: no versions. Filter: '{filter}'")
        return []
    for vr in versions:
        vr["description"] = vr.get("description","")
        vr["user_id"] = vr.get("user_id","")
        if not get_tags_and_aliases:
            vr.pop("tags", None)
    print(f"Found {len(versions)} model versions")
    return versions

def get_model_details(vr):
    model_uri = f"models:/{vr['name']}/{vr['version']}"
    try:
        mlflow_model = get_mlflow_model.get(model_uri)
        mlflow_model = mlflow_model["mlflow_model"]
        return mlflow_model["model_flavor"], mlflow_model["model_size_bytes"]
    except mlflow.exceptions.MlflowException as e:
        print(f"WARNING: Cannot get MLflow model for {model_uri}: {e}")
        return "?", -1


def _to_dict(model, key, func, tags_and_aliases_as_string):
    kv_list = model.get(key)
    if kv_list:
        model[key] = func(kv_list)
        dct = func(kv_list)
        if tags_and_aliases_as_string:
            dct = object_utils.dict_to_json(dct)
        model[key] = dct

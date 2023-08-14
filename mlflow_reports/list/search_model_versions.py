"""
Search for model versions and return Pandas DataFrame.
"""

import numpy as np
import pandas as pd
import mlflow

from mlflow_reports.data import get_mlflow_model
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator, SearchModelVersionsIterator
from mlflow_reports.common import mlflow_utils
from . import list_utils


def search(filter=None,
        get_tags_and_aliases = False,
        tags_and_aliases_as_string = False,
        get_model_details = False,
        unity_catalog = False
    ):
    if unity_catalog:
        mlflow_utils.use_unity_catalog()
    mlflow_client = get_mlflow_client()
    if mlflow_utils.is_calling_databricks():
        versions = _list_model_versions_databricks(mlflow_client, filter, get_tags_and_aliases, get_model_details)
    else:
        versions = _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details)
    if len(versions) == 0:
        return pd.DataFrame()
    if tags_and_aliases_as_string:
        for vr in versions:
            list_utils.kv_list_to_dict(vr, "tags", mlflow_utils.mk_tags_dict, True)
    df = pd.DataFrame.from_dict(versions)
    df = df.replace(np.nan, "", regex=True)
    list_utils.to_datetime(df, "creation_timestamp")
    list_utils.to_datetime(df, "last_updated_timestamp")
    return df


def _list_model_versions_databricks(mlflow_client, filter, get_tags_and_aliases, get_model_details):
    if filter:
        return _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details)
    models = SearchRegisteredModelsIterator(mlflow_client)
    models = list(models)   
    num_models = len(models)   
    print(f"Found {num_models} models")
    versions = []
    for j, model in enumerate(models):
        print(f"Processing {j+1}/{num_models} model '{model['name']}'")
        filter = f"name='{model['name']}'"
        vrs = _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details)
        if vrs:
            versions += vrs
    print(f"Found {len(versions)} model versions")
    return versions


def _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details):
    versions = SearchModelVersionsIterator(mlflow_client, filter=filter)
    versions = list(versions)
    if len(versions) == 0:
        print(f"WARNING: no versions. Filter: '{filter}'")
        return []
    for vr in versions:
        vr["description"] = vr.get("description","") # NOTE: not present if empty
        vr["user_id"] = vr.get("user_id","") # NOTE: not present if empty
        if not get_tags_and_aliases:
            vr.pop("tags", None)
        if get_model_details:
            flavor, size = _get_model_details(vr)
            vr["model_flavor"] = flavor
            vr["model_size"] = size 
    sfilter = f'for filter "{filter}"' if filter else ""
    print(f"Found {len(versions)} model versions {sfilter}")
    return versions


def _get_model_details(vr):
    model_uri = f"models:/{vr['name']}/{vr['version']}"
    try:
        mlflow_model = get_mlflow_model.get(model_uri)
        mlflow_model = mlflow_model["mlflow_model"]
        return mlflow_model["model_flavor"], mlflow_model["model_size_bytes"]
    except mlflow.exceptions.MlflowException as e:
        print(f"WARNING: Cannot get MLflow model for {model_uri}: {e}")
        return "?", -1

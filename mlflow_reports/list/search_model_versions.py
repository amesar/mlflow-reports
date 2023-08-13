"""
Search for model versions and return Pandas DataFrame.
"""

import mlflow
import pandas as pd

from mlflow_reports.data import get_mlflow_model
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator, SearchModelVersionsIterator
from mlflow_reports.common import mlflow_utils
from . import list_utils


def search(filter=None,
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
            list_utils.kv_list_to_dict(vr, "tags", mlflow_utils.mk_tags_dict, True)
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

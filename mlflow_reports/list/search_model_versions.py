"""
Search for model versions and return Pandas DataFrame.
"""

import numpy as np
import pandas as pd
import mlflow

from mlflow_reports.data import get_mlflow_model
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common.http_iterators import SearchRegisteredModelsIterator
from mlflow_reports.common import mlflow_utils
from . import list_utils


def search(filter=None,
        get_tags_and_aliases = True,
        tags_and_aliases_as_string = False,
        get_model_details = False,
        get_search_object_again = False,
        unity_catalog = False
    ):
    mlflow_utils.use_unity_catalog(unity_catalog)
    mlflow_client = get_mlflow_client()
    if mlflow_utils.is_calling_databricks():
        versions = _list_model_versions_databricks(mlflow_client, filter, get_tags_and_aliases, get_model_details, get_search_object_again)
    else:
        versions = _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details, get_search_object_again)
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


def _list_model_versions_databricks(mlflow_client, filter, get_tags_and_aliases, get_model_details, get_search_object_again):
    """
    Databricks search_model_version differs from OSS one in that it requires a filter.
    So to fetch all versions of all models, we have to loop over all models first.

    https://github.com/mlflow/mlflow/issues/7967
    [BUG] search_model_versions request contract differs between OSS and Databricks - 2023-03-06

    https://databricks.atlassian.net/browse/ML-29535
    Databricks MLflowClient.search_model_versions() requires model_name in filter but OSS does not - Databricks JIRA
    """

    if filter:
        return _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details, get_search_object_again)
    models = SearchRegisteredModelsIterator(mlflow_client)
    models = list(models)
    num_models = len(models)
    print(f"Found {num_models} models")
    versions = []
    for j, model in enumerate(models):
        print(f"Processing {j+1}/{num_models} model '{model['name']}'")
        filter = f"name='{model['name']}'"
        vrs = _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details, get_search_object_again)
        if vrs:
            versions += vrs
    print(f"Found {len(versions)} model versions")
    return versions


def _list_model_versions(mlflow_client, filter, get_tags_and_aliases, get_model_details, get_search_object_again):
    """
    Standard OSS search_model_version documented filter.
    """
    versions = mlflow_utils.search_model_versions(mlflow_client, filter, get_search_object_again)
    if len(versions) == 0:
        print(f"WARNING: No model versions. Filter: '{filter}'")
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

"""
Search for model versions and return Pandas DataFrame.
"""

import copy
import numpy as np
import pandas as pd
import mlflow

from mlflow_reports.data import get_mlflow_model
from mlflow_reports.common import mlflow_utils
from . import list_utils


def search(
        filter = None,
        prefix = None,
        get_tags_and_aliases = False,
        get_model_details = False,
        unity_catalog = False
    ):
    if mlflow_utils.is_calling_databricks():
        versions = _list_model_versions_databricks(filter, prefix, get_tags_and_aliases, get_model_details, unity_catalog)
    else:
        versions = _list_model_versions(filter, get_tags_and_aliases, get_model_details, unity_catalog)
    return versions


def as_pandas_df(versions, max_description=None):
    if len(versions) == 0:
        return pd.DataFrame()
    versions = copy.deepcopy(versions)
    df = pd.DataFrame.from_dict(versions)
    df = df.replace(np.nan, "", regex=True)
    df = df.sort_values(["name", "version"], ascending=[True, False])
    if "description" in df and max_description:
        df["description"] = df["description"].str[:max_description]
    list_utils.to_datetime(df, [ "creation_timestamp", "last_updated_timestamp"])
    return df


def _list_model_versions_databricks(filter, prefix, get_tags_and_aliases, get_model_details, unity_catalog):
    """
    Databricks search_model_version differs from OSS one in that it requires a filter.
    So to fetch all versions of all models, we have to loop over all models first.

    https://github.com/mlflow/mlflow/issues/7967
    [BUG] search_model_versions request contract differs between OSS and Databricks - 2023-03-06

    https://databricks.atlassian.net/browse/ML-29535
    Databricks MLflowClient.search_model_versions() requires model_name in filter but OSS does not - Databricks JIRA
    """

    if filter:
        return _list_model_versions(filter, get_tags_and_aliases, get_model_details, unity_catalog)

    models = mlflow_utils.search_registered_models(unity_catalog=unity_catalog)
    models = list_utils.filter_registered_models_by_prefix(models, prefix)
    num_models = len(models)
    print(f"Found {num_models} models")

    versions = []
    for j, model in enumerate(models):
        print(f"Processing {j+1}/{num_models} model '{model['name']}'")
        filter = f"name='{model['name']}'"
        _versions = _list_model_versions(filter, get_tags_and_aliases, get_model_details, unity_catalog)
        if _versions:
            versions += _versions
    print(f"Found {len(versions)} model versions")
    return versions


def _list_model_versions(filter, get_tags_and_aliases, get_model_details, unity_catalog):
    """
    Standard OSS search_model_version documented filter.
    """
    versions = mlflow_utils.search_model_versions(filter, get_tags_and_aliases, unity_catalog=unity_catalog)
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
        mlflow_model = mlflow_model.get("mlflow_model")
        return mlflow_model.get("model_flavor"), mlflow_model.get("model_size_bytes")
    except mlflow.exceptions.MlflowException as e:
        print(f"WARNING: Cannot get MLflow model for {model_uri}: {e}")
        return "?", -1

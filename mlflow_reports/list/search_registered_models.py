"""
Search for registered models return Pandas DataFrame.
"""

import numpy as np
import pandas as pd

from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common import mlflow_utils
from . import list_utils


def search(filter=None,
        prefix = None,
        get_tags_and_aliases = True,
        tags_and_aliases_as_string = False,
        get_search_object_again = False,
        unity_catalog = False
    ):
    mlflow_utils.use_unity_catalog(unity_catalog)
    mlflow_client = get_mlflow_client()
    models = mlflow_utils.search_registered_models(mlflow_client, filter, get_search_object_again)
    if prefix:
        models = [ m for m in models if m["name"].startswith(prefix)]
    models = sorted(models, key=lambda x: x["name"])
    print(f"Found {len(models)} registered models")

    for model in models:
        list_utils.kv_list_to_dict(model, "tags", mlflow_utils.mk_tags_dict, tags_and_aliases_as_string)
        list_utils.kv_list_to_dict(model, "aliases", mlflow_utils.mk_aliases_dict, tags_and_aliases_as_string)
        model.pop("latest_versions", None)
        if not get_tags_and_aliases:
            model.pop("tags", None)
            model.pop("aliases", None)

    if len(models) == 0:
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(models)
    df = df.replace(np.nan, "", regex=True)
    list_utils.to_datetime(df, "creation_timestamp")
    list_utils.to_datetime(df, "last_updated_timestamp")

    return df

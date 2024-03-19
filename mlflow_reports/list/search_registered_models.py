"""
Search for registered models
"""

import copy
import numpy as np
import pandas as pd

from mlflow_reports.common import mlflow_utils
from mlflow_reports.common.pandas_utils import move_column
from . import list_utils


def search(filter=None, get_tags_and_aliases=False, unity_catalog=False):
    """
    :return: Returns registered models as list of Dicts.
    """
    models = mlflow_utils.search_registered_models(filter, get_tags_and_aliases, unity_catalog)
    print(f"Found {len(models)} registered models")
    models = sorted(models, key=lambda x: x["name"])
    return models


def as_pandas_df(models, prefix=None, tags_and_aliases_as_string=False):
    if len(models) == 0:
        return pd.DataFrame()
    models = copy.deepcopy(models)
    if prefix:
        models = [ m for m in models if m["name"].startswith(prefix)]
    models = sorted(models, key=lambda x: x["name"])
    for model in models:
        list_utils.kv_list_to_dict(model, "tags", mlflow_utils.mk_tags_dict, tags_and_aliases_as_string)
        list_utils.kv_list_to_dict(model, "aliases", mlflow_utils.mk_aliases_dict, tags_and_aliases_as_string)
        model.pop("latest_versions", None)

    df = pd.DataFrame.from_dict(models)
    df = df.replace(np.nan, "", regex=True)
    df = move_column(df, "user_id", index=1)
    list_utils.to_datetime(df, ["creation_timestamp", "last_updated_timestamp"])
    return df

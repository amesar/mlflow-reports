"""
Search for experiments.
"""

import numpy as np
import pandas as pd
from mlflow_reports.client import mlflow_client
from mlflow_reports.common import mlflow_utils
from . import list_utils


def search(filter=None, view_type=None, max_results=None):
    experiments = mlflow_client.search_experiments(filter, view_type, max_results)
    experiments = list(experiments)
    print(f"Found {len(experiments)} experiments")
    return experiments


def as_pandas_df(experiments, tags_and_aliases_as_string=False):
    if len(experiments) == 0:
        return pd.DataFrame()
    for exp in experiments:
        list_utils.kv_list_to_dict(exp, "tags", mlflow_utils.mk_tags_dict, tags_and_aliases_as_string)
    df = pd.DataFrame.from_dict(experiments)
    df = df.replace(np.nan, "", regex=True)
    list_utils.to_datetime(df, ["creation_time", "last_update_time"])
    return df

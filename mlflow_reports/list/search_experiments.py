"""
Search for experiments and return Pandas DataFrame.
"""

import numpy as np
import pandas as pd

from mlflow_reports.common.http_iterators import SearchExperimentsIterator
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common import mlflow_utils
from . import list_utils


def search(filter=None, view_type="ACTIVE_ONLY", tags_and_aliases_as_string=False, max_results=1000):
    mlflow_client = get_mlflow_client()
    experiments = SearchExperimentsIterator(mlflow_client, filter=filter, view_type=view_type, max_results=max_results)
    experiments = list(experiments)
    print(f"Found {len(experiments)} experiments")
    for exp in experiments:
        list_utils.kv_list_to_dict(exp, "tags", mlflow_utils.mk_tags_dict, tags_and_aliases_as_string)
    return experiments


def search_as_pandas_df(filter=None, view_type="ACTIVE", tags_and_aliases_as_string=False):
    experiments =  search(filter, view_type, tags_and_aliases_as_string)
    if len(experiments) == 0:
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(experiments)
    df = df.replace(np.nan, "", regex=True)
    list_utils.to_datetime(df, "creation_time")
    list_utils.to_datetime(df, "last_update_time")

    return df

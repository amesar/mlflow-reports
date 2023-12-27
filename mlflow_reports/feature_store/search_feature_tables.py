"""
Search/list of all feature tables.
From undocumented Databricks endpoint api/2.0/feature-store/feature-tables/search.
Only returns feature tables created by "older" FeatureStoreClient.
Note this does NOT return Unity Catalog feature tables created with new FeatureEngineeringClient.
"""

import numpy as np
import pandas as pd
from mlflow_reports.client.feature_store_client import FeatureStoreClient
from mlflow_reports.list import list_utils

client = FeatureStoreClient()

def search():
    tables = client.search()
    print(f"Found {len(tables)} feature tables")
    return tables

def search_as_pandas_df():
    tables = search()
    if len(tables) == 0:
        return pd.DataFrame()
    df = pd.DataFrame.from_dict(tables)
    df = df.replace(np.nan, "", regex=True)
    list_utils.to_datetime(df, [ "creation_timestamp", "last_updated_timestamp" ] )
    return df

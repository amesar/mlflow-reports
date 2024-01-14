"""
Client for undocumented Databricks REST API for feature store.
Base endpoint: api/2.0/feature-store/feature-tables.
"""

from . http_client import dbx_20_client
from mlflow_reports.common.http_iterators import FeatureTablesIterator


class FeatureStoreClient:

    def __init__(self):
        self.client = dbx_20_client

    def search(self):
        """
        Endpoint: api/2.0/feature-store/feature-tables/search
        """
        tables = FeatureTablesIterator(self.client)
        return list(tables)

    def get_table(self, table_name, get_from_search=False):
        """
        Endpoint: api/2.0/feature-store/feature-tables/get
        """
        if get_from_search:
            tables = self.search()
            matches = [ tbl for tbl in tables if tbl.get("name") == table_name ]
            if len(matches) > 0:
                return { "feature_table": matches[0] }
            return {}
        else:
            return self.client.get(self._mk_uri("get"), params = { "name": table_name} )

    def _mk_uri(self, resource):
        return f"feature-store/feature-tables/{resource}"

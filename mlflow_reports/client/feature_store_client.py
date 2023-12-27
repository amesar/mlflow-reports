"""
Client for undocumented Databricks REST API for feature store.
Base endpoint: api/2.0/feature-store/feature-tables.
"""

from . http_client import DatabricksHttpClient
from mlflow_reports.common.http_iterators import FeatureTablesIterator


class FeatureStoreClient:

    def __init__(self):
        self.client = DatabricksHttpClient()

    def search(self):
        """
        Endpoint: api/2.0/feature-store/feature-tables/search
        """
        tables = FeatureTablesIterator(self.client)
        return list(tables)

    def get_table(self, table_name):
        """
        Endpoint: api/2.0/feature-store/feature-tables/get
        """
        return self.client.get(self._mk_uri("get"), params = { "name": table_name} )

    def _mk_uri(self, resource):
        return f"feature-store/feature-tables/{resource}"

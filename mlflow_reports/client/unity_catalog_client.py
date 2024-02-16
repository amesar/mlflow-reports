from typing import Dict, List
from mlflow_reports.common.uc_http_iterators import (
    SearchUcRegisteredModelsIterator
)
from . http_client import dbx_21_client


class UnityCatalogClient:
    def __init__(self):
        self.client = dbx_21_client

    def get_permissions(self, model_name: str) -> List:
        return self.client.get(f"unity-catalog/permissions/function/{model_name}")

    def get_effective_permissions(self, model_name: str) -> List:
        return self.client.get(f"unity-catalog/effective-permissions/function/{model_name}")

    def get_table(self, table_name: str) -> Dict:
        return self.client.get(f"unity-catalog/tables/{table_name}")

    def list_registered_models(self, catalog_name: str, schema_name, max_results=None) -> List:
        return list(SearchUcRegisteredModelsIterator(self.client, catalog_name, schema_name, max_results=max_results))



client = UnityCatalogClient()

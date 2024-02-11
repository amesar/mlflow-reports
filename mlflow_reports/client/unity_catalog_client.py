from typing import Dict, List
from . http_client import dbx_21_client


class UnityCatalogClient:
    def __init__(self):
        self.client = dbx_21_client

    def get_permissions(self, model_name: str) -> List:
        resource = f"unity-catalog/permissions/function/{model_name}"
        return self.client.get(resource)

    def get_effective_permissions(self, model_name: str) -> List:
        resource = f"unity-catalog/effective-permissions/function/{model_name}"
        return self.client.get(resource)

    def get_table(self, table_name: str) -> Dict:
        return client.get(f"unity-catalog/tables/{table_name}")


client = UnityCatalogClient()

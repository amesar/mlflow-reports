from typing import Dict
from . http_client import dbx_20_client, get_mlflow_client


class DatabricksClient:
    
    def __init__(self):
        self.mlflow_client = get_mlflow_client()

    def get_workspace_status(self) -> Dict:
        return dbx_20_client.get("workspace/get-status")
    
    def get_registered_model(self, model_name: str) -> Dict:
        return self.mlflow_client.get("databricks/registered-models/get", {"name": model_name} )

    def get_table_lineage(self, table_name: str) -> Dict:
        return dbx_20_client.get("lineage-tracking/table-lineage", {"table_name": table_name})


client = DatabricksClient()

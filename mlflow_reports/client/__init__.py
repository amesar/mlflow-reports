USER_AGENT = "mlflow-report/1.0.0"

from . mlflow_client import client as mlflow_client
from . databricks_client import client as databricks_client
from . unity_catalog_client import client as unity_catalog_client

def get_mlflow_client(unity_catalog):
    from . mlflow_client import client, uc_client
    return uc_client if unity_catalog else client

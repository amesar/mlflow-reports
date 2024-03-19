USER_AGENT = "mlflow-report/1.0.0"

from . mlflow_client import client as mlflow_client
from . databricks_client import client as databricks_client
from . unity_catalog_client import client as unity_catalog_client
#from mlflow_reports.common.mlflow_utils import is_unity_catalog_model

def _is_unity_catalog_model(model_name):
    return "." in model_name

def get_mlflow_client(uc_switch_or_model_name):
    from . mlflow_client import client, uc_client
    if isinstance(uc_switch_or_model_name, bool):
        return uc_client if uc_switch_or_model_name else client
    else: # assume its a model name
        return uc_client if _is_unity_catalog_model(uc_switch_or_model_name) else client

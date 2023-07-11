from mlflow_reports.client.http_client import DatabricksHttpClient, HttpClient
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common.mlflow_utils import is_unity_catalog_model

dbx_client = DatabricksHttpClient()
dbx_client_21 = HttpClient("api/2.1")

def add_experiment_permissions(experiment):
    experiment_id = experiment["experiment_id"]
    _add(experiment,
        _call(f"permissions/experiments/{experiment_id}/permissionLevels", "permission_levels"),
        _call(f"permissions/experiments/{experiment_id}")
    )


def add_model_permissions(reg_model):
    model_name = reg_model["name"]
    if is_unity_catalog_model(model_name):
        resource = f"unity-catalog/permissions/function/{model_name}"
        perms = dbx_client_21.get(resource)
        resource = f"unity-catalog/effective-permissions/function/{model_name}"
        effective_perms = dbx_client_21.get(resource)
        reg_model["permissions"] = {
            "permissions": perms,
            "effective_permissions": effective_perms,
        }
    else:
        model_id = reg_model["id"]
        _add(reg_model, 
            _call(f"permissions/registered-models/{model_id}/permissionLevels","permission_levels"),
            _call(f"permissions/registered-models/{model_id}")
         )


def _add(obj, perm_levels, perms):
    if perm_levels and perms:
        obj["permissions"] = {}
        if perm_levels: # returns dict with keys: permission_levels
            obj["permissions"] = { **perm_levels }
        if perms: # returns dict with keys: 'object_id', 'object_type', 'access_control_list' 
            obj["permissions"]["permissions"] = perms


def _call(resource, root=None):
    try:
        return dbx_client.get(resource)

    except MlflowReportsException as e:

        # Calling OSS Mlflow
        if e.http_status_code == 404:
            print(f"WARNING: Databricks permissions API call failed: {e}")
            return None

        # Calling Databricks but apparently a notebook experiment fails for get permissions
        else: 
            print(f"WARNING: Databricks permissions API call failed: {e}")
            error = { "error": str(e) }
            if root:
                error = { root: error }
            return error

from mlflow_reports.client.http_client import DatabricksHttpClient
from mlflow_reports.common import MlflowReportsException

dbx_client = DatabricksHttpClient()

def add_experiment_permissions(experiment):
    experiment_id = experiment["experiment_id"]
    _add(experiment,
        _call(f"permissions/experiments/{experiment_id}/permissionLevels", "permission_levels"),
        _call(f"permissions/experiments/{experiment_id}")
    )


def add_model_permissions(reg_model):
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

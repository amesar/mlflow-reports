from mlflow_reports.client.http_client import DatabricksHttpClient, HttpClient
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common.mlflow_utils import is_unity_catalog_model
from mlflow_reports.common.mlflow_utils import is_calling_databricks
from mlflow_reports.common import exception_utils

dbx_client = DatabricksHttpClient()

def add_experiment_permissions(experiment):
    if not is_calling_databricks():
        return
    experiment_id = experiment["experiment_id"]
    _add(experiment,
        _call(f"permissions/experiments/{experiment_id}/permissionLevels", "permission_levels"),
        _call(f"permissions/experiments/{experiment_id}")
    )

class UcPermissionsClient:
    def __init__(self):
        self.client = HttpClient("api/2.1")

    def get_permissions(self, model_name):
        resource = f"unity-catalog/permissions/function/{model_name}"
        return self.client.get(resource)

    def get_effective_permissions(self, model_name):
        resource = f"unity-catalog/effective-permissions/function/{model_name}"
        return self.client.get(resource)

uc_perms_client = UcPermissionsClient()


def add_model_permissions(reg_model):
    if not is_calling_databricks():
        return
    model_name = reg_model["name"]
    if is_unity_catalog_model(model_name):
        reg_model["permissions"] = {
            "permissions": uc_perms_client.get_permissions(model_name),
            "effective_permissions": uc_perms_client.get_effective_permissions(model_name)
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
            msg = "Databricks permissions API call failed"
            print(f"ERROR: {msg}: {e}")
            error = exception_utils.to_dict(e, msg)
            if root:
                error = { root: error }
            return error

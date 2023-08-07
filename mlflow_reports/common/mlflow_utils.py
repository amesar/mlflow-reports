from dataclasses import dataclass

import mlflow
from mlflow.exceptions import RestException
from mlflow_reports.client.http_client import get_mlflow_client
from mlflow_reports.common import MlflowReportsException

http_client = get_mlflow_client()


def get_experiment(exp_id_or_name):
    """
    Gets an experiment either by ID or name.
    :param: http_client - MLflowClient.
    :param: exp_id_or_name - Experiment ID or name..
    :return: Experiment object.
    """
    try:
        rsp = http_client.get("experiments/get-by-name", {"experiment_name": exp_id_or_name})
    except MlflowReportsException as e:
        try:
            rsp = http_client.get("experiments/get", {"experiment_id": exp_id_or_name})
        except RestException as e:
            raise MlflowReportsException(f"Cannot find experiment ID or name '{exp_id_or_name}'. Client: {http_client}'. Ex: {e}")
    return rsp["experiment"]


def get_registered_model(model_name, get_permissions):
    """
    Get a registered model. Response depends upon:
       1. databricks/registered-models/get - standard call
       2. databricks/registered-models/get - custom Databricks call that simply has an extra "id" field needed
          to subsequently call to get permissions
    """
    if get_permissions:
        resource = "databricks/registered-models/get"
        try:
            model = http_client.get(resource, {"name": model_name} )
            return model["registered_model_databricks"]
        except MlflowReportsException as e:
            print(f"WARNING: Databricks API call '{resource}' failed: {e}")
            model = http_client.get(f"registered-models/get", {"name": model_name} )
            return model["registered_model"]
    else:
        model = http_client.get(f"registered-models/get", {"name": model_name} )
        return model["registered_model"]


def build_artifacts(run_id, artifact_path, artifact_max_level, level=0):
    """
    Build recursive tree of calls to 'artifacts/list' API endpoint.
    :param run_id: Run ID.
    :param artifact_path: Relative artifact path.
    :param artifact_max_level: Levels to recurse.
    :return: Nested dict with list of artifacts representing tree node info.
    """
    res = _build_artifacts(run_id, artifact_path, artifact_max_level, level)
    summary = {
        "artifact_max_level": artifact_max_level,
        "num_artifacts": res.num_artifacts,
        "num_bytes": res.num_bytes,
        "num_levels": res.num_levels
    }
    return { **{ "summary": summary }, **res.artifacts }


def _build_artifacts(run_id, artifact_path, artifact_max_level, level=0):
    @dataclass()
    class Result:
        artifacts: dict = None
        num_bytes: int = 0
        num_artifacts: int = 0
        num_levels: int = 0
        def __repr__(self):
            return f"{self.num_bytes} {self.num_artifacts} {self.num_levels}"

    if level == artifact_max_level:
        return Result({}, 0, 0, level)

    artifacts = http_client.get(f"artifacts/list", { "run_id": run_id, "path": artifact_path })
    if level > artifact_max_level:
        return Result(artifacts, 0, 0, level)

    files = artifacts.get("files", None)
    level += 1
    new_level = level
    num_bytes, num_artifacts = (0,0)
    if files:
        for _,artifact in enumerate(files):
            num_bytes += int(artifact.get("file_size",0)) or 0
            if artifact["is_dir"]:
                res = _build_artifacts(run_id, artifact["path"], artifact_max_level, level)
                new_level = max(new_level, res.num_levels)
                num_bytes += res.num_bytes
                num_artifacts += res.num_artifacts
                artifact["artifacts"] = res.artifacts
            else:
                num_artifacts += 1
    return Result(artifacts, num_bytes, num_artifacts, new_level)


def mk_tags_dict(tags_array):
    """
    Transform a list of key/value elements to a dict.
    """
    if tags_array is None:
        return {}
    return { x["key"]:x["value"] for x in tags_array }


def is_unity_catalog_model(model_name):
    return "." in model_name


def use_unity_catalog():
    mlflow.set_registry_uri("databricks-uc")
    print("New mlflow.registry_uri:",mlflow.get_registry_uri())


_is_calling_into_databricks = None
             
def is_calling_databricks(dbx_client=None):
    """
    Are we calling Databricks MLflow? Check by making call to Databricks-specific API endpoint.
    """
    from mlflow_reports.client.http_client import DatabricksHttpClient
    
    global _is_calling_into_databricks
    dbx_client = dbx_client or DatabricksHttpClient()
    if _is_calling_into_databricks is None:
        try:
            dbx_client.get("workspace/get-status")
            return False # Should never get here
        except MlflowReportsException as e:
            _is_calling_into_databricks =  e.http_status_code == 400
            print(f"Calling Databricks MLflow: {_is_calling_into_databricks}")
    return _is_calling_into_databricks

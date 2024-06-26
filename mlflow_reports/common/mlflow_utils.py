from mlflow.exceptions import RestException
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.client import mlflow_client, databricks_client, get_mlflow_client


def get_experiment(exp_id_or_name):
    """
    Gets an experiment either by ID or name.
    :param: exp_id_or_name - Experiment ID or name..
    :return: Experiment object.
    """
    try:
        rsp = mlflow_client.get_experiment_by_name(exp_id_or_name)
    except MlflowReportsException as e:
        try:
            rsp = mlflow_client.get_experiment(exp_id_or_name)
        except RestException as e:
            raise MlflowReportsException(f"Cannot find experiment ID or name '{exp_id_or_name}'. Client: {mlflow_client}'. Ex: {e}")
    return rsp["experiment"]


def get_registered_model(model_name, get_permissions):
    """
    Get a registered model. Response depends upon:
       1. databricks/registered-models/get - standard call
       2. databricks/registered-models/get - custom Databricks call that simply has an extra "id" field needed
          to subsequently call to get permissions
    """
    _mlflow_client = get_mlflow_client(model_name)
    if is_calling_databricks() and get_permissions and not is_unity_catalog_model(model_name):
        try:
            model = databricks_client.get_registered_model(model_name)
            return model["registered_model_databricks"]
        except MlflowReportsException as e:
            print(f"WARNING: Databricks API call failed: {e}")
            model = _mlflow_client.get_registered_model(model_name)
            return model["registered_model"]
    else:
        model = _mlflow_client.get_registered_model(model_name)
        return model["registered_model"]


def search_registered_models(filter=None, get_search_object_again=False, unity_catalog=False):
    """
    Search for registered models.
    For Databricks UC, need to call 'registered-models/get' again for each
    returned model since aliases and tags are not returned. This is much
    slower obviously especially for a large number of models. For 328 models,
    just the search takes 6 seconds and with the extra get call takes 178 seconds.

    https://databricks.atlassian.net/browse/ES-834105
    UC-ML MLflow search_registered_models and search_model_versions do not return tags and aliases
    """
    def _mk_filter(name):
        return f"name='{name}'"
    _mlflow_client = get_mlflow_client(unity_catalog)
    models = _mlflow_client.search_registered_models(filter=filter)
    if get_search_object_again:
        print(f"Calling get_registered_model() again for {len(models)} models")
        models = [ _mlflow_client.search_registered_models(_mk_filter(m["name"])) for m in models ]
        return [ m["registered_model"] for m in models]
    else:
        return models


def search_model_versions(filter=None, get_search_object_again=False, unity_catalog=False):
    """
    Search for model versions.
    See  https://github.com/mlflow/mlflow/issues/9783 (no alias)

    https://databricks.atlassian.net/browse/ES-834105
    UC-ML MLflow search_registered_models and search_model_versions do not return tags and aliases

    https://github.com/mlflow/mlflow/issues/9783
    MlflowClient.search_model_versions does not return aliases
    """

    _mlflow_client = get_mlflow_client(unity_catalog)
    versions = _mlflow_client.search_model_versions(filter=filter)
    if not get_search_object_again:
        return versions

    print(f"Calling get_model_version() again for {len(versions)} versions")
    versions2 = []
    failed = []
    for vr in versions:
        try:
            vr2 = mlflow_client.get_model_version(vr["name"], vr["version"])
            versions2.append(vr2)
        except MlflowReportsException as e:
            # NOTE: Failing for: Unsupported function securable kind FUNCTION_REGISTERED_MODEL_DELTASHARING"
            print(f"ERROR: 'model-versions/get' failed. Ex: {e}")
            failed.append(vr)
    if len(failed) > 0:
        print(f"WARNING: {len(failed)} calls to 'model-versions/get' failed")
        for vr in failed:
            msg = { "name": vr["name"], "version": vr["version"] }
            print(f"  WARNING: {msg} call to 'model-versions/get' failed")
    return [ vr["model_version"] for vr in versions2]


def mk_tags_dict(tags_array):
    """
    Transform a list of key/value items to a dict.
    """
    return mk_key_value_array_dict(tags_array, "key", "value")

def mk_aliases_dict(aliases_array):
    """
    Transform a list of alias/version items to a dict.
    """
    return mk_key_value_array_dict(aliases_array, "alias", "version")

def mk_key_value_array_dict(kv_array, key_name, value_name):
    """
    Transforms a list of 2 item dicts to a dict.
    Example:  [{'key': 'k1', 'value': 'v1'}, {'key': 'k2', 'value': 'v2'}] ==> {'k1': 'v1', 'k2': 'v2' }
    """
    if kv_array is None:
        return {}
    return { x[key_name]:x[value_name] for x in kv_array }


def is_unity_catalog_model(model_name):
    return "." in model_name


def has_error(dct):
    return "warning" in dct or "error" in dct


_is_calling_into_databricks = None

def is_calling_databricks():
    """
    Are we calling Databricks MLflow? Check by making call to Databricks-specific API endpoint.
    """

    global _is_calling_into_databricks
    if _is_calling_into_databricks is None:
        try:
            databricks_client.get_workspace_status()
            return False # Should never get here
        except MlflowReportsException as e:
            _is_calling_into_databricks =  e.http_status_code == 400
            print(f"Calling Databricks MLflow: {_is_calling_into_databricks}")
    return _is_calling_into_databricks


def get_latest_run(experiment_id_or_name):
    """
    Return the latest run (by 'start_time') of an experiment..
    """
    exp = get_experiment(experiment_id_or_name)
    runs = mlflow_client.search_runs(exp["experiment_id"], order_by=["start_time desc"])
    print(f"Found {len(runs)} runs for experiment '{experiment_id_or_name}'")
    return runs[0] if runs else None

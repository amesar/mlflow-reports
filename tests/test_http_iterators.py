"""
Test the MLflow HTTP object iterators (Run, Experiment, Registered Model and Model Versions).
"""

from mlflow.entities import ViewType
import mlflow

from mlflow_reports.client.http_client import mlflow_client as http_client
from mlflow_reports.common.http_iterators import (
    SearchExperimentsIterator,
    SearchRegisteredModelsIterator,
    SearchModelVersionsIterator,
    SearchRunsIterator
)
from . iterators_test_utils import (
    list_experiments,
    create_experiment,
    delete_experiments,
    delete_models,
    mk_test_object_name_default,
    TEST_OBJECT_PREFIX
)
from . utils_test import create_run

mlflow_client = mlflow.MlflowClient()


# ==== Test SearchExperimentsIterator

_default_num_runs = 5

def _create_experiment(num_runs=_default_num_runs):
    experiment = create_experiment(mlflow_client)
    for _ in range(num_runs):
        with mlflow.start_run():
            mlflow.log_metric("m1", 0.1)
    return experiment

def _create_experiments(num_experiments, num_runs=_default_num_runs):
    delete_experiments(mlflow_client)
    experiments = list_experiments(mlflow_client)
    assert len(experiments) == 0
    return [ _create_experiment(num_runs).experiment_id for _ in range(num_experiments) ]

def _run_test_search_experiments(num_experiments, max_results):
    _create_experiments(num_experiments)
    experiments1 = list_experiments(mlflow_client)
    experiments2 = SearchExperimentsIterator(http_client, max_results=max_results)
    assert len(experiments1) == len(list(experiments2))

# == basic tests

def test_search_experiments_max_results_LT_num_experiments():
    _run_test_search_experiments(10, 5)

def test_search_experiments_max_results_EQ_num_experiments():
    _run_test_search_experiments(10, 10)

def test_search_experiments_max_results_GT_num_experiments():
    _run_test_search_experiments(10, 20)

def test_search_experiments_max_results_custom():
    num_experiments = 101
    max_results = 20
    _create_experiments(num_experiments)
    experiments1 = list_experiments(mlflow_client)
    assert len(experiments1) == num_experiments
    experiments2 = SearchExperimentsIterator(http_client, max_results=max_results)
    assert len(experiments1) == len(list(experiments2))


# == search_experiments view_type tests
#
# Since experiments are tombstoned and not physically,
# we have to write some non-obvious logic to account for deleted experiments.
#

_num_exps = 5
_num_exps_deleted = 2
_max_results = 100

def _run_test_deleted_experiments():
    num_runs = 5
    num_exps_to_delete = 2
    exp_ids = _create_experiments(_num_exps, num_runs)
    exps_del_01 = list(SearchExperimentsIterator(http_client, view_type=ViewType.DELETED_ONLY, max_results=_max_results))
    exp_ids_deleted = exp_ids[:num_exps_to_delete]
    run_ids_deleted = list(SearchRunsIterator(http_client, exp_ids_deleted))
    assert len(run_ids_deleted) == num_exps_to_delete * num_runs

    # delete experiments
    for exp_id in exp_ids_deleted:
        mlflow_client.delete_experiment(exp_id)

    # check that experiments are actually deleted
    for exp_id in exp_ids_deleted:
        exp = mlflow_client.get_experiment(exp_id)
        assert exp.lifecycle_stage == "deleted"

    # check that runs of deleted experiments are themselves deleted
    for run in run_ids_deleted:
        run = mlflow_client.get_run(run["info"]["run_id"])
        assert run.info.lifecycle_stage == "deleted"
    run_ids_deleted = list(SearchRunsIterator(http_client, exp_ids_deleted, view_type=ViewType.DELETED_ONLY))
    assert len(run_ids_deleted) == num_exps_to_delete * num_runs

    exps_del_02 = list(SearchExperimentsIterator(http_client, view_type=ViewType.DELETED_ONLY, max_results=_max_results))
    return len(exps_del_02) - len(exps_del_01)


def test_deleted_experiments_default():
    _run_test_deleted_experiments()
    exps = list(SearchExperimentsIterator(http_client, max_results=_max_results))
    assert _num_exps - _num_exps_deleted == len(exps)

def test_deleted_experiments_view_active_only():
    _run_test_deleted_experiments()
    exps = list(SearchExperimentsIterator(http_client, view_type=ViewType.ACTIVE_ONLY, max_results=_max_results))
    assert _num_exps - _num_exps_deleted == len(exps)

def test_deleted_experiments_view_deleted_only():
    num_deleted = _run_test_deleted_experiments()
    assert _num_exps_deleted == num_deleted

def test_deleted_experiments_view_deleted_all():
    exps1 = list(SearchExperimentsIterator(http_client, view_type=ViewType.ALL, max_results=_max_results))
    _run_test_deleted_experiments()
    exps2 = list(SearchExperimentsIterator(http_client, view_type=ViewType.ALL, max_results=_max_results))
    assert _num_exps == len(exps2) - len(exps1)


# ==== Test SearchRegisteredModelsIterator

# == test search models 1

def _init_test_search_models():
    delete_experiments(mlflow_client)
    delete_models(mlflow_client)

def _create_models(num_models):
    delete_models(mlflow_client)
    models = mlflow_client.search_registered_models()
    assert len(models) == 0
    for _ in range( num_models):
        model_name = mk_test_object_name_default()
        mlflow_client.create_registered_model(model_name)


def test_search_models_like():
    _init_test_search_models()
    num_models = 10
    max_results = 5
    _create_models(num_models)
    models = list(SearchRegisteredModelsIterator(http_client, max_results))
    new_prefix = f"{TEST_OBJECT_PREFIX}_new"
    for j in range(0,4):
        model = models[j]
        new_name = model["name"].replace(TEST_OBJECT_PREFIX, new_prefix)
        mlflow_client.rename_registered_model(model["name"], new_name)
    filter = f"name like '{new_prefix}%'"
    models2 = SearchRegisteredModelsIterator(http_client, filter=filter)
    assert 4 == len(list(models2))

# == test search models 2

def _run_test_search_models(num_models, max_results):
    _create_models(num_models)
    models1 = mlflow_client.search_registered_models()
    assert len(models1) == num_models
    models2 = SearchRegisteredModelsIterator(http_client, max_results)
    assert len(models1) == len(list(models2))


def test_search_models_max_results_LT_num_models():
    _run_test_search_models(10, 5)

def test_search_models_max_results_EQ_num_models():
    _run_test_search_models(10, 10)

def test_search_models_max_results_GT_num_models():
    _run_test_search_models(10, 20)

def test_search_models_max_results_custom():
    num_models = 101
    max_results = 20
    _create_models(num_models)
    models1 = mlflow_client.search_registered_models(max_results=num_models)
    assert len(models1) == num_models
    models2 = SearchRegisteredModelsIterator(http_client, max_results)
    assert len(models1) == len(list(models2))

def test_search_models_max_results_non_default():
    MAX_RESULTS_DEFAULT = 100
    num_models = 101
    max_results = 20
    _create_models(num_models)
    models1 = mlflow_client.search_registered_models()
    assert len(models1) == MAX_RESULTS_DEFAULT
    models2 = SearchRegisteredModelsIterator(http_client, max_results)
    assert len(list(models2)) == num_models


# ==== Test SearchModelVersionsIterator

# order_by - Error message:
#   mlflow.exceptions.RestException: INVALID_PARAMETER_VALUE:
#   Invalid attribute key 'foo' specified
#   Valid keys are '{'version_number', 'creation_timestamp', 'last_updated_timestamp', 'name'}'


def _create_model_version(model_name):
    run, _ = create_run()
    source = f"runs:/{run.info.run_id}/model"
    return mlflow_client.create_model_version(model_name, source, run.info.run_id)

def _create_versions(num_models, num_versions):
    delete_models(mlflow_client)
    models = mlflow_client.search_registered_models()
    assert len(models) == 0
    model_names = [ mk_test_object_name_default() for _ in range(num_models) ]
    for model_name in model_names:
        mlflow_client.create_registered_model(model_name)
        for _ in range(num_versions):
            _create_model_version(model_name)
    return model_names


def test_search_versions_basic():
    model_names = _create_versions(2, 2)
    versions = list(SearchModelVersionsIterator(http_client))
    assert len(model_names) == 2
    assert len(versions) == 2 * 2


def test_search_versions_filter_by_name():
    model_names = _create_versions(2, 2)
    filter = f"name='{model_names[0]}'"
    versions = list(SearchModelVersionsIterator(http_client, filter=filter))
    assert len(versions) == 2

# NOTE: No error if you specifiy an unsupported column
def test_search_versions_filter_by_run_id():
    _create_versions(2, 2)
    versions = list(SearchModelVersionsIterator(http_client))
    vr = versions[0]
    run_id = vr["run_id"]
    filter = f"run_id='{run_id}'"
    versions = list(SearchModelVersionsIterator(http_client, filter=filter))
    assert len(versions) == 1


def test_search_versions_order_by_version():
    model_names = _create_versions(2, 2)
    filter = f"name='{model_names[0]}'"
    order_by = ["version_number"]
    versions = list(SearchModelVersionsIterator(http_client, filter=filter, order_by=order_by))
    assert len(versions) == 2
    assert versions[0]["version"] == "1"

def test_search_versions_order_by_version_desc():
    model_names = _create_versions(2, 2)
    filter = f"name='{model_names[0]}'"
    order_by = ["version_number DESC"]
    versions = list(SearchModelVersionsIterator(http_client, filter=filter, order_by=order_by))
    assert len(versions) == 2
    assert versions[0]["version"] == "2"

def test_search_versions_order_by_creation_timestamp_desc():
    model_names = _create_versions(2, 2)
    filter = f"name='{model_names[0]}'"
    order_by = ["creation_timestamp DESC"]
    versions = list(SearchModelVersionsIterator(http_client, filter=filter, order_by=order_by))
    assert len(versions) == 2
    assert versions[0]["version"] == "2"

# NOTE: FAILS
def _fails_test_search_versions_order_by_run_ud():
    model_names = _create_versions(2, 2)
    filter = f"name='{model_names[0]}'"
    order_by = ["run_id"]
    versions = list(SearchModelVersionsIterator(http_client, filter=filter, order_by=order_by))
    assert len(versions) == 2


# ==== Test SearchRunsIterator

# == basic tests

def test_search_runs_simple():
    num_runs = 2
    exp = _create_experiment(num_runs)
    runs = mlflow_client.search_runs(exp.experiment_id)
    assert num_runs == len(runs)
    iterator = SearchRunsIterator(http_client, exp.experiment_id)
    runs = list(iterator)
    assert num_runs == len(runs)

def test_search_runs():
    num_runs = 120
    max_results = 22
    exp = _create_experiment(num_runs)
    runs = mlflow_client.search_runs(exp.experiment_id)
    assert num_runs == len(runs)
    iterator = SearchRunsIterator(http_client, exp.experiment_id, max_results)
    runs = list(iterator)
    assert num_runs == len(runs)

def test_runs_search_empty():
    num_runs = 0
    max_results = 22
    exp = _create_experiment(num_runs)
    runs = mlflow_client.search_runs(exp.experiment_id)
    assert num_runs == len(runs)
    iterator = SearchRunsIterator(http_client, exp.experiment_id, max_results)
    runs = list(iterator)
    assert num_runs == len(runs)


# == search_runs view_type tests

_num_runs = 5
_num_runs_deleted = 2

def _run_test_deleted_runs():
    exp = _create_experiment(_num_runs)
    runs = list(SearchRunsIterator(http_client, exp.experiment_id))
    assert _num_runs == len(runs)
    for j in range(_num_runs_deleted):
        mlflow_client.delete_run(runs[j]["info"]["run_id"])
    return exp, runs


def test_deleted_runs_default():
    exp, runs = _run_test_deleted_runs()
    runs = list(SearchRunsIterator(http_client, exp.experiment_id))
    assert _num_runs - _num_runs_deleted == len(runs)

def test_deleted_runs_view_active_only():
    exp, runs = _run_test_deleted_runs()
    runs = list(SearchRunsIterator(http_client, exp.experiment_id, view_type=ViewType.ACTIVE_ONLY))
    assert _num_runs - _num_runs_deleted == len(runs)

def test_deleted_runs_view_deleted_only():
    exp, runs = _run_test_deleted_runs()
    runs = list(SearchRunsIterator(http_client, exp.experiment_id, view_type=ViewType.DELETED_ONLY))
    assert _num_runs_deleted == len(runs)

def test_deleted_runs_view_all():
    exp, runs = _run_test_deleted_runs()
    runs = list(SearchRunsIterator(http_client, exp.experiment_id, view_type=ViewType.ALL))
    assert _num_runs == len(runs)


# == other tests

# Stress test - fails because of connection timeout
def __test_search_runs_too_many():
    num_runs = 1200
    max_results = 500
    exp = _create_experiment(num_runs)
    runs = mlflow_client.search_runs(exp.experiment_id)
    assert len(runs) == 1000
    iterator = SearchRunsIterator(http_client, exp.experiment_id, max_results)
    runs = list(iterator)
    assert num_runs == len(runs)

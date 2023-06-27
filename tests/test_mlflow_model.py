from mlflow.exceptions import MlflowException

from mlflow_reports.data import get_mlflow_model
from . utils_test import create_model_version, create_run, model_artifact_path, to_str


# ==== Test without runs

def test_runs_uri():
    run, _ = create_run()
    _do_test_models_uri(run, _mk_runs_uri(run))

def test_models_uri():
    vr, run = create_model_version()
    _do_test_models_uri(run, _mk_models_uri(vr))


def _do_test_models_uri(run1, model_uri):
    _mm = get_mlflow_model.get(model_uri)
    mm = _mm["mlflow_model"]
    _assert_model(mm, run1)
    assert not "run" in _mm


# ==== Test with runs

def test_runs_uri_with_run():
    run, _ = create_run()
    _do_test_runs_uri_with_run(run, _mk_runs_uri(run))

def test_models_uri_with_run():
    vr, run = create_model_version()
    _do_test_runs_uri_with_run(run, _mk_models_uri(vr))


def _do_test_runs_uri_with_run(run1, model_uri):
    run1, _ = create_run()
    model_uri = _mk_runs_uri(run1)

    _mm = get_mlflow_model.get(model_uri, get_run=True)
    mm = _mm["mlflow_model"]
    _assert_model(mm,run1)

    run = _mm.get("run") 
    assert run
    info = run["info"]
    assert info["run_id"] == run1.info.run_id
    assert to_str(info["experiment_id"]) == run1.info.experiment_id

    exp = _mm.get("experiment") 
    assert exp
    assert to_str(exp["experiment_id"]) == run1.info.experiment_id
    assert exp["name"] == info["_experiment_name"]


# ==== Test failed URIs

def test_fail_bad_uri(): 
    try:
        get_mlflow_model.get("foo")
        assert False
    except MlflowException:
        pass

def test_fail_non_existent_runs_uri(): 
    model_uri = "runs:/foo/bar"
    try:
        get_mlflow_model.get(model_uri)
        assert False
    except MlflowException:  # RestException
        pass

def test_fail_non_existent_models_uri(): 
    model_uri = "models:/model/1"
    try:
        get_mlflow_model.get(model_uri)
        assert False
    except MlflowException:  # RestException
        pass


# ==== Helpers

def _assert_model(mm, run):
    assert mm.get("artifact_path") == model_artifact_path
    assert mm.get("run_id") == run.info.run_id
    flavors = mm.get("flavors")
    assert flavors
    assert len(flavors) == 2
    assert flavors.get("python_function")
    assert flavors.get("sklearn")

def _mk_runs_uri(run):
    return f"runs:/{run.info.run_id}/{model_artifact_path}"

def _mk_models_uri(vr):
    return f"models:/{vr.name}/{vr.version}"

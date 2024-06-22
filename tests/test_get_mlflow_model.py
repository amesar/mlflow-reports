from mlflow_reports.data import get_mlflow_model
from . utils_test import (
    create_model_version,
    create_run,
    model_artifact_path,
    mk_runs_uri, mk_models_uri,
    to_str
)

# ==== Test without runs

def test_runs_uri():
    run, _ = create_run()
    _do_test_without_run(run, mk_runs_uri(run))

def test_models_uri():
    vr, run, _ = create_model_version()
    _do_test_without_run(run, mk_models_uri(vr))


def _do_test_without_run(run1, model_uri):
    _mm = get_mlflow_model.get(model_uri)
    mm = _mm["mlflow_model"]
    _assert_model(mm, run1)
    assert not "run" in _mm


# ==== Test with runs

def test_runs_uri_with_run():
    run, _ = create_run()
    _do_test_with_runs(run, mk_runs_uri(run))

def test_models_uri_with_run():
    vr, run, _ = create_model_version()
    _do_test_with_runs(run, mk_models_uri(vr))


def _do_test_with_runs(run1, model_uri):
    run1, _ = create_run()
    model_uri = mk_runs_uri(run1)

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


# ==== Test bad URIs

def test_fail_bad_uri(): 
    _assert_bad_uri("foo")

def test_fail_non_existent_runs_uri(): 
    _assert_bad_uri("runs:/foo/bar")

def test_fail_non_existent_models_uri(): 
    _assert_bad_uri("models:/model/1")


# ==== Helpers

def _assert_bad_uri(model_uri):
    dct = get_mlflow_model.get(model_uri)
    dct = dct["mlflow_model"]
    assert "error" in dct

def _assert_model(mm, run):
    assert mm.get("artifact_path") == model_artifact_path
    assert mm.get("run_id") == run.info.run_id
    flavors = mm.get("flavors")
    assert flavors
    assert len(flavors) == 2
    assert flavors.get("python_function")
    assert flavors.get("sklearn")

import mlflow

from mlflow.exceptions import MlflowException
from mlflow_reports.mlflow_model import mlflow_model_manager

from . utils_test import (
    create_model_version,
    create_run,
    model_artifact_path,
    mk_runs_uri, mk_models_uri,
    to_str
)

mlflow_client = mlflow.MlflowClient()

# ==== Test basic 

def test_runs_uri():
    run1, exp1 = create_run()
    model_uri = mk_runs_uri(run1)
    _mm = mlflow_model_manager.get(model_uri)
    _assert(_mm, run1, exp1)
    assert not "registered_model" in _mm
    assert not "model_version" in _mm


def test_models_uri():
    vr1, run1, exp1 = create_model_version()
    model_uri = mk_models_uri(vr1)

    _mm = mlflow_model_manager.get(model_uri)
    _assert(_mm, run1, exp1)
    _assert_model_version(vr1, _mm)
    _assert_registered_model(vr1, _mm)


# ==== Test failed URIs

def test_fail_bad_uri(): 
    try:
        mlflow_model_manager.get("foo")
        assert False
    except MlflowException:
        pass

def test_fail_non_existent_runs_uri(): 
    model_uri = "runs:/foo/bar"
    try:
        mlflow_model_manager.get(model_uri)
        assert False
    except MlflowException:  # RestException
        pass

def test_fail_non_existent_models_uri(): 
    model_uri = "models:/model/1"
    try:
        mlflow_model_manager.get(model_uri)
        assert False
    except MlflowException:  # RestException
        pass


# ==== Helpers

def _assert(_mm, run1, exp1):
    _assert_uber(_mm)
    _assert_mlflow_model(run1, _mm)
    _assert_run(run1, _mm)
    _assert_experiment(exp1, _mm)

def _assert_uber(_mm):
    manifest = _mm.get("manifest")
    assert manifest
    assert "model_uri" in manifest
    assert "model_uri" in manifest
    model_uris = manifest.get("model_uris")
    assert model_uris
    assert len(model_uris) >= 2

def _assert_mlflow_model(run1, _mm):
    mm = _mm.get("mlflow_model")
    assert mm
    assert mm.get("artifact_path") == model_artifact_path
    assert mm.get("run_id") == run1.info.run_id
    flavors = mm.get("flavors")
    assert flavors
    assert len(flavors) == 2
    assert flavors.get("python_function")
    assert flavors.get("sklearn")

def _assert_run(run1, _mm):
    run2 = _mm.get("run")
    assert run2
    info2 = run2.get("info")
    assert info2.get("run_id") == run1.info.run_id
    assert to_str(info2.get("experiment_id")) == run1.info.experiment_id
    assert info2.get("artifact_uri") == run1.info.artifact_uri

def _assert_experiment(exp1, _mm):
    exp2 = _mm.get("experiment")
    exp2 = _mm.get("experiment")
    assert exp2
    assert to_str(exp2.get("experiment_id")) == exp1.experiment_id
    assert exp2.get("name") == exp1.name
    assert exp2.get("artifact_location") == exp1.artifact_location

def _assert_model_version(vr1, _mm):
    vr2 = _mm.get("model_version")
    assert vr2
    assert vr2.get("name") == vr1.name

def _assert_registered_model(vr1, _mm):
    rm2 = _mm.get("registered_model")
    assert rm2
    rm1 = mlflow_client.get_registered_model(vr1.name)
    assert rm1
    assert rm2.get("name") == rm1.name

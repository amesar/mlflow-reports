from mlflow_reports.common import MlflowReportsException
from mlflow_reports.data import get_registered_model, get_model_version
from . utils_test import create_registered_model
from . utils_test import assert_enriched_tags
#from mlflow_reports.common.dump_utils import dump_as_json
from mlflow_reports.client.mlflow_client import client


def _get_versions(model_dct):
    model_dct = model_dct.get("registered_model")
    model_name = model_dct["name"]
    filter = f"name='{model_name}'"
    versions =  client.search_model_versions(filter=filter)
    return [ get_model_version.get(vr["name"], vr["version"], get_expanded=True)["model_version"] for vr in versions ]

def test_get_model():
    model1 = create_registered_model()
    _model2 = get_registered_model.get(model1.name)
    model2 = _model2.get("registered_model")
    versions = _get_versions(_model2)
    assert len(versions) == 3
    assert model2
    assert_model(model1, model2)
    assert_enriched_tags(model2, True)
    assert not "version_runs" in _model2


def _do_test_get_model_with_runs(artifact_max_level=-1):
    model1 = create_registered_model()
    _model2 = get_registered_model.get(model1.name, get_run=True, get_versions=True, artifact_max_level=artifact_max_level)
    model2 = _model2.get("registered_model")
    assert model2
    assert_model(model1, model2)
    versions = _get_versions(_model2)
    assert len(versions) == 3

    assert_enriched_tags(model2, True) # OK
    for vr in versions:
        assert_enriched_tags(vr, True) # FAILS 

    runs2 =  _model2.get("version_runs")
    assert runs2
    for _run in runs2.values():
        run = _run["run"]
        assert_enriched_tags(run["info"], True)
        if artifact_max_level > -1:
            assert "artifacts" in _run
        else:
            assert not "artifacts" in _run

def test_get_model_with_runs():
    _do_test_get_model_with_runs()

def test_get_model_with_runs_and_artifacts():
    _do_test_get_model_with_runs(999)


def test_get_model_raw():
    model1 = create_registered_model()
    _model2 = get_registered_model.get(model1.name, get_raw=True)
    model2 = _model2.get("registered_model")
    assert model2
    versions = model2.get("latest_versions")
    assert len(versions) == 3
    assert_model(model1, model2)
    assert_enriched_tags(model2, False)
    for vr in versions:
        assert_enriched_tags(vr, False)


def test_get_fail():
    try:
        get_registered_model.get("foobar")
        assert False
    except MlflowReportsException as e:
        assert e.http_status_code == 404


def assert_model(model1, model2):
    assert model1.name == model2.get("name")
    #assert len(model1.latest_versions) == len(model2.get("latest_versions")) #  NOTE: mlflow 2.14.1 - gone

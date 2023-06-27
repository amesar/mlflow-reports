import mlflow
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.data import get_registered_model
from . utils_test import create_registered_model
from . utils_test import assert_enriched_tags
from mlflow_reports.common.object_utils import dump_as_json

client = mlflow.MlflowClient()


def test_get_rm():
    rm1 = create_registered_model()
    _rm2 = get_registered_model.get(rm1.name)
    dump_as_json(_rm2)
    rm2 = _rm2.get("registered_model")
    assert rm2
    versions = rm2.get("latest_versions")
    assert len(versions) == 3
    assert_rm(rm1, rm2)
    assert_enriched_tags(rm2, True)
    for vr in versions:
        assert_enriched_tags(vr, True)
    assert not "version_runs" in _rm2


def _do_test_get_rm_with_runs(artifact_max_level=-1):
    rm1 = create_registered_model()
    _rm2 = get_registered_model.get(rm1.name, get_runs=True, artifact_max_level=artifact_max_level)
    dump_as_json(_rm2)
    rm2 = _rm2.get("registered_model")
    assert rm2
    versions = rm2.get("latest_versions")
    assert len(versions) == 3
    assert_rm(rm1, rm2)

    assert_enriched_tags(rm2, True)
    for vr in versions:
        assert_enriched_tags(vr, True)

    runs2 =  _rm2.get("version_runs")
    assert runs2
    for _run in runs2.values():
        run = _run["run"]
        assert_enriched_tags(run["info"], True)
        if artifact_max_level > -1:
            assert "artifacts" in _run
        else:
            assert not "artifacts" in _run

def test_get_rm_with_runs():
    _do_test_get_rm_with_runs()

def test_get_rm_with_runs_and_artifacts():
    _do_test_get_rm_with_runs(999)


def test_get_rm_raw():
    rm1 = create_registered_model()
    _rm2 = get_registered_model.get(rm1.name, get_raw=True)
    dump_as_json(_rm2)
    rm2 = _rm2.get("registered_model")
    assert rm2
    versions = rm2.get("latest_versions")
    assert len(versions) == 3
    assert_rm(rm1, rm2)
    assert_enriched_tags(rm2, False)
    for vr in versions:
        assert_enriched_tags(vr, False)


def test_get_fail():
    try:
        get_registered_model.get("foobar")
        assert False
    except MlflowReportsException as e:
        assert e.http_status_code == 404


def assert_rm(rm1, rm2):
    assert rm1.name == rm2.get("name")
    assert len(rm1.latest_versions) == len(rm2.get("latest_versions"))

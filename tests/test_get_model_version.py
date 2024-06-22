from mlflow_reports.common import MlflowReportsException
from mlflow_reports.common import model_version_utils
from mlflow_reports.data import get_model_version
from . utils_test import assert_enriched_tags
from . utils_test import create_model_version
from . import test_get_run
from mlflow_reports.common.dump_utils import dump_as_json


def test_get_version():
    vr1, _, _ = create_model_version()
    _vr2 = get_model_version.get(vr1.name, vr1.version)
    assert not "run" in _vr2
    vr2 = _vr2.get("model_version")
    assert_version(vr1, vr2)
    assert_enriched_tags(vr2, True)


def _do_test_get_version_with_run(artifact_max_level=-1):
    vr1, run1, _ = create_model_version()
    _vr2 = get_model_version.get(vr1.name, vr1.version, get_expanded=True, artifact_max_level=artifact_max_level)
    vr2 = _vr2.get("model_version")
    assert_version(vr1, vr2)
    assert_enriched_tags(vr2, True)

    _run2 = _vr2.get("run")
    assert _run2

    run2 = _run2.get("run")
    assert run2
    test_get_run.assert_run(run1, run2)

    if artifact_max_level > -1:
        assert "artifacts" in _run2
    else:
        assert not "artifacts" in _run2

def test_get_version_with_run(): # FAILS
    _do_test_get_version_with_run()

def test_get_version_with_run_and_artifacts():
    _do_test_get_version_with_run(5)


def test_get_version_raw():
    vr1, _, _ = create_model_version()
    _vr2 = get_model_version.get(vr1.name, vr1.version, get_raw=True)
    dump_as_json(_vr2)
    assert len(_vr2) == 1
    vr2 = _vr2.get("model_version")
    assert vr2
    assert_version(vr1, vr2, False)
    assert_enriched_tags(vr2, False)


def test_get_fail():
    try:
        get_model_version.get("foo", "12") # NOTE: version cannot be int but must be an "int" string!
        assert False
    except MlflowReportsException as e:
        assert e.http_status_code == 404


def assert_version(vr1, vr2, enriched=True):
    assert vr1.version == vr2.get("version")
    assert vr1.name == vr2.get("name")
    assert vr1.current_stage == vr2.get("current_stage")
    assert vr1.source == vr2.get("source")

    if not enriched:
        return 

    run_model_uri = vr2.get("_run_model_download_uri")
    assert run_model_uri
    assert run_model_uri == vr1.source

    reg_model_uri = vr2.get("_reg_model_download_uri")
    assert reg_model_uri
    assert reg_model_uri == model_version_utils.get_reg_model_download_uri(vr2)


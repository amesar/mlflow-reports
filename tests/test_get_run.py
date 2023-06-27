from mlflow_reports.common import MlflowReportsException
from mlflow_reports.data import get_run
from . utils_test import create_run, assert_enriched_tags


def test_get_run():
    run1, exp1 = create_run()
    rsp = get_run.get(run1.info.run_id)
    run2 = assert_run(run1, rsp)
    assert_enriched_tags(run2["info"], True)
    assert exp1.name == run2["info"]["_experiment_name"]
    assert not "artifacts" in rsp


def test_get_run_artifacts():
    run1, exp1 = create_run()
    rsp = get_run.get(run1.info.run_id, artifact_max_level=5)
    run2 = assert_run(run1, rsp)
    assert_enriched_tags(run2["info"], True)
    assert exp1.name == run2["info"]["_experiment_name"]
    artifacts = rsp.get("artifacts")
    assert artifacts 
    assert "summary" in artifacts


def test_get_run_raw():
    run1, _ = create_run()
    run2 = get_run.get(run1.info.run_id, get_raw=True)
    run2 = assert_run(run1, run2)
    assert_enriched_tags(run2["info"], False)


def test_get_fail():
    try:
        get_run.get("foo")
        assert False
    except MlflowReportsException as e:
        assert e.http_status_code == 404


def assert_run(run1, run2):
    if "run" in run2:
        run2 = run2.get("run")
    assert not "artifacts" in run2
    assert run2
    assert run1.info.run_id == run2["info"]["run_id"]
    return run2

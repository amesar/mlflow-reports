from mlflow_reports.common import mlflow_utils 
from mlflow_reports.common import MlflowReportsException
from mlflow_reports.data import get_experiment

from . utils_test import create_experiment, create_run, assert_enriched_tags
from . import test_get_run
from mlflow_reports.common.dump_utils import dump_as_json


# == 

def test_get_by_id():
    exp1 = create_experiment()
    rsp = get_experiment.get(exp1.experiment_id)
    exp2 = rsp["experiment"]
    dump_as_json(rsp)
    _assert_experiment(exp1, exp2)
    assert_enriched_tags(exp2, True)
    assert not "runs" in rsp


def test_get_by_name():
    exp1 = create_experiment()
    rsp = get_experiment.get(exp1.experiment_id)
    exp2 = rsp["experiment"]
    _assert_experiment(exp1, exp2)
    assert_enriched_tags(exp2, True)
    assert not "runs" in rsp


def test_get_fail():
    create_experiment()
    try:
        mlflow_utils.get_experiment("foo")
        assert False
    except MlflowReportsException as e:
        assert e.http_status_code == 404


def test_get_raw():
    exp1 = create_experiment()
    rsp = get_experiment.get(exp1.experiment_id, get_raw=True)
    exp2 = rsp["experiment"]
    _assert_experiment(exp1, exp2)
    assert_enriched_tags(exp2, False)


def test_get_with_runs():
    run1, exp1 = create_run()
    rsp = get_experiment.get(exp1.experiment_id, get_runs=True)
    exp2 = rsp["experiment"]
    _assert_experiment(exp1, exp2)
    assert_enriched_tags(exp2, True)

    runs = rsp.get("runs")
    assert runs
    assert len(runs) == 1
    run2 = runs[0]
    test_get_run.assert_run(run1, run2)
    assert not "artifacts" in run2


def test_get_with_runs_with_artifacts():
    run1, exp1 = create_run()
    rsp = get_experiment.get(exp1.experiment_id, get_runs=True, artifact_max_level=999)
    exp2 = rsp["experiment"]
    _assert_experiment(exp1, exp2)
    assert_enriched_tags(exp2, True)

    runs = rsp.get("runs")
    assert runs
    assert len(runs) == 1
    run2 = runs[0]
    test_get_run.assert_run(run1, run2)
    assert "artifacts" in run2


def _assert_experiment(exp1, exp2):
    assert exp1.experiment_id == str(exp2["experiment_id"]) # NOTE: OSS returns int instead of string as per doc

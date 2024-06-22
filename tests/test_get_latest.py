"""
Test get latest model version and get latest run.
"""

import time
from mlflow_reports.common.model_version_utils import get_latest_model_version
from mlflow_reports.common.mlflow_utils import get_latest_run
from . utils_test import create_experiment, create_run
from . test_http_iterators import _create_versions


def test_latest_model_version():
    model_names = _create_versions(1, 2)
    latest_vr = get_latest_model_version(model_names[0])
    assert latest_vr
    assert latest_vr["version"] == "2"


def test_latest_run():
    exp = create_experiment()
    create_run(exp)
    time.sleep(1) # since we're ordering by 'start_time'
    run2, _ = create_run(exp)
    latest_run = get_latest_run(exp.name)
    assert latest_run
    assert run2.info.run_id == latest_run["info"]["run_id"]

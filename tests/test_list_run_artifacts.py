from tempfile import NamedTemporaryFile
import mlflow

from mlflow_reports.common.artifact_utils import list_run_artifacts
#from mlflow_reports.common.dump_utils import dump_as_json
from . utils_test import create_experiment


content = "so many eight-thousanders"
content_size = len(content)

# == Test no levels

def _create_level_0():
    create_experiment()
    with mlflow.start_run() as run:
        mlflow.log_metric("rmse", 0.789)
    return run


def test_create_no_levels_check_0_level():
    _run_test_create(_create_level_0, max_level=0, num_levels=0, num_artifacts=0)

def test_create_no_levels_check_1_level():
    _run_test_create(_create_level_0, max_level=1, num_levels=1, num_artifacts=0)

def test_create_no_levels_check_3_level():
    _run_test_create(_create_level_0, max_level=3, num_levels=1, num_artifacts=0)


# == Test one level 

def _create_level_1():
    create_experiment()
    with mlflow.start_run() as run:
        with NamedTemporaryFile(prefix="file_", suffix=".txt", mode="w") as f:
            _log_artifact(f, "")
        with NamedTemporaryFile(prefix="file_", suffix=".txt", mode="w") as f:
            _log_artifact(f, "")
    return run


def test_create_1_levels_check_0_level():
    _run_test_create(_create_level_1, max_level=0, num_levels=0, num_artifacts=0)

def test_create_1_levels_check_1_level():
    _run_test_create(_create_level_1, max_level=1, num_levels=1, num_artifacts=2)

def test_create_1_levels_check_2_level():
    _run_test_create(_create_level_1, max_level=2, num_levels=1, num_artifacts=2)


# == Test two levels

def _create_level_2():
    create_experiment()
    dir = "model"
    with mlflow.start_run() as run:
        with NamedTemporaryFile(prefix="file_", suffix=".txt", mode="w") as f:
            _log_artifact(f, "")
        with NamedTemporaryFile(prefix="MLModel_", suffix=".txt", mode="w") as f2:
            _log_artifact(f2, dir)
        with NamedTemporaryFile(prefix="pickle", suffix=".txt", mode="w") as f2:
            _log_artifact(f2, dir)
    return run


def test_create_2_levels_check_0_level():
    _run_test_create(_create_level_2, max_level=0, num_levels=0, num_artifacts=0)

def test_create_2_levels_check_1_level():
    _run_test_create(_create_level_2, max_level=1, num_levels=1, num_artifacts=1)

def test_create_2_levels_check_2_level():
    _run_test_create(_create_level_2, max_level=2, num_levels=2, num_artifacts=3)

def test_create_2_levels_check_3_level():
    _run_test_create(_create_level_2, max_level=3, num_levels=2, num_artifacts=3)


# == Test three levels

def _create_level_3():
    create_experiment()
    dir = "spark-model"
    with mlflow.start_run() as run:
        with NamedTemporaryFile(prefix="file_", suffix=".txt", mode="w") as f:
            _log_artifact(f, "")
        with NamedTemporaryFile(prefix="MLModel_", suffix=".txt", mode="w") as f2:
            _log_artifact(f2, dir)
        with NamedTemporaryFile(prefix="info", suffix=".txt", mode="w") as f2:
            _log_artifact(f2, dir)
        with NamedTemporaryFile(prefix="0_VectorAssembler_e717399caab5_", suffix=".txt", mode="w") as f2:
            _log_artifact(f2, f"{dir}/sparkml")
    return run


def test_create_3_levels_check_0_level():
    _run_test_create(_create_level_3, max_level=0, num_levels=0, num_artifacts=0)

def test_create_3_levels_check_1_level():
    _run_test_create(_create_level_3, max_level=1, num_levels=1, num_artifacts=1)

def test_create_3_levels_check_2_level():
    _run_test_create(_create_level_3, max_level=2, num_levels=2, num_artifacts=3)

def test_create_3_levels_check_3_level():
    _run_test_create(_create_level_3, max_level=3, num_levels=3, num_artifacts=4)

def test_create_3_levels_check_4_level():
    _run_test_create(_create_level_3, max_level=4, num_levels=3, num_artifacts=4)


# == Helper functions

def _run_test_create(create_func, max_level, num_levels, num_artifacts):
    run = create_func()
    res = list_run_artifacts(run.info.run_id, "", max_level)
    #dump_as_json(res["summary"])
    _assert_result(res, content_size*num_artifacts, num_artifacts, num_levels, max_level)

def _log_artifact(f, artifact_path):
    f.file.write(content)
    f.file.close()
    mlflow.log_artifact(f.name, artifact_path)

def _assert_result(res, num_bytes, num_artifacts, num_levels, artifact_max_level):
    res = res["summary"]
    assert res["artifact_max_level"] == artifact_max_level
    assert res["num_bytes"] == num_bytes
    assert res["num_artifacts"] == num_artifacts
    assert res["num_levels"] == num_levels

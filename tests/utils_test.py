import time
from tempfile import NamedTemporaryFile
import shortuuid
import mlflow
import mlflow.sklearn
from . sklearn_utils import create_sklearn_model

print("Mlflow path:", mlflow.__file__)
print("MLflow version:", mlflow.__version__)

mlflow_client = mlflow.MlflowClient()
sklearn_model = create_sklearn_model()
model_artifact_path = "sklearn-model"


def now():
    return round(time.time())


def mk_uuid():
    return shortuuid.uuid()


def mk_runs_uri(run):
    return f"runs:/{run.info.run_id}/{model_artifact_path}"
    

def mk_models_uri(vr):
    return f"models:/{vr.name}/{vr.version}"


def to_str(x):
    """
    REST API returns experiment_id as 'int' although it is documented as 'string'
    """
    return str(x)


def create_experiment():
    exp_name = mk_uuid()
    mlflow.set_experiment(exp_name)
    exp = mlflow_client.get_experiment_by_name(exp_name)
    for run in mlflow_client.search_runs(exp.experiment_id):
        mlflow_client.delete_run(run.info.run_id)
    return exp


def create_run(exp=None):
    if not exp:
        exp = create_experiment()
    content = "Bears invade inner suburbs"
    with mlflow.start_run() as run:
        mlflow.log_param("max_depth", 5)
        mlflow.log_metric("rmse", 0.786)
        mlflow.set_tag("info", "hi")
        with NamedTemporaryFile(prefix="file_", suffix=".txt", mode="w") as f:
            f.file.write(content)
            f.file.close()
            mlflow.log_artifact(f.name, "")
        mlflow.sklearn.log_model(sklearn_model, model_artifact_path)
    run = mlflow_client.get_run(run.info.run_id)
    return run, exp


def create_model_version(stage=None, archive_existing_versions=False):
    """
    Create a model version, its registered model and run
    """
    model_name = mk_uuid()
    mlflow_client.create_registered_model(model_name)
    run, exp = create_run()
    source = f"{run.info.artifact_uri}/{model_artifact_path}"
    desc = "My version desc"
    tags = { "city": "yaxchilan" }
    vr = mlflow_client.create_model_version(model_name, source, run.info.run_id, description=desc, tags=tags)
    if stage:
        vr = mlflow_client.transition_model_version_stage(model_name, vr.version, stage, archive_existing_versions)
    return vr, run, exp


def create_registered_model():
    def create_version(reg_model_name, stage, exp):
        run, _ = create_run(exp)
        vr = mlflow_client.create_model_version(reg_model_name, run.info.artifact_uri, run.info.run_id)
        mlflow_client.transition_model_version_stage(reg_model_name, vr.version, stage)
    reg_model_name = mk_uuid()
    mlflow_client.create_registered_model(reg_model_name)
    exp = create_experiment()
    create_version(reg_model_name, "production", exp)
    create_version(reg_model_name, "staging", exp)
    create_version(reg_model_name, "archived", exp)
    return mlflow_client.get_registered_model(reg_model_name)


def delete_experiment(exp):
    mlflow_client.delete_experiment(exp.experiment_id)


def compare_dirs(d1, d2):
    from filecmp import dircmp
    def _compare_dirs(dcmp):
        if len(dcmp.diff_files) > 0 or len(dcmp.left_only) > 0 or len(dcmp.right_only) > 0:
            return False
        for sub_dcmp in dcmp.subdirs.values():
            if not _compare_dirs(sub_dcmp):
                return False
        return True
    return _compare_dirs(dircmp(d1, d2))


def assert_enriched_tags(dct, do_assert):
    enriched_keys = [ k for k in dct.keys() if k.startswith("_") ]
    if do_assert:
        assert len(enriched_keys) > 0
    else:
        assert len(enriched_keys) == 0


def dump_tags(tags, msg=""):
    print(f"==== {len(tags)} Tags:",msg)
    tags = dict(sorted(tags.items()))
    for k,v in tags.items():
        print(f"  {k}: {v}")

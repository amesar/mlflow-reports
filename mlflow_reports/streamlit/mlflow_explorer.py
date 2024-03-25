import copy
import streamlit as st
from mlflow_reports.list import search_registered_models, search_model_versions, search_experiments
from mlflow_reports.data import get_registered_model, get_model_version, get_experiment, get_run
from mlflow_reports.mlflow_model.mlflow_model_utils import get_model_artifact
from mlflow_reports.common import explode_utils
from mlflow_reports.common.timestamp_utils import now
from mlflow_reports.client import mlflow_client


def main():
    help="Explore MLlflow objects - registered models, model versions, model signatures, experiments and runs"
    st.title("MLflow API Explorer", help=help)

    st.write(f"MLflow tracking server: {mlflow_client}")

    help = "Add additional fields such as readable timestamps and related objects response JSON"
    raw = not st.toggle("Enrich", key="enrich", help=help)

    tab_list, tab_details = st.tabs([ "List", "Details" ] )
    with tab_list:
        do_tab_list()
    with tab_details:
        do_tab_details(raw)


# ==============
# List objects

def do_tab_list():
    st.header("List MLflow Objects")

    tab_models, tab_versions, tab_experiments, tab_runs = \
        st.tabs(["Registered models", "Model versions", "Experiments", "Runs" ])

    with tab_models:
        do_registered_models()

    with tab_versions:
        do_model_versions()
    with tab_experiments:
        do_experiments()
    with tab_runs:
        do_runs()


def do_registered_models():
    def refresh(filter, unity_catalog):
        filter = filter or None
        models = search_registered_models.search(filter=filter, unity_catalog=unity_catalog)
        st.write(f"Retrieved {len(models)} registered models at {now()}")
        st.session_state.models = models
        return models

    models = st.session_state.models if "models" in st.session_state else []
    st.subheader("_Registered Models_")

    unity_catalog = st.toggle("Unity Catalog", key="use_uc_registered_models")

    help = """
See [MlflowClient.search_registered_models()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). Example: _name='sklearn_wine'_ or _name like '%sklearn%'_.
"""
    filter = st.text_input("Search filter", key="model_filter", help=help)

    if st.button("Refresh", key="refresh_registered_models"):
        models = refresh(filter, unity_catalog)

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if models:
        with tab_table:
            df = search_registered_models.as_pandas_df(models)
            st.write(df)
        with tab_json:
            st.write(models)


def do_model_versions():
    def refresh(filter, unity_catalog):
        filter = filter or None
        versions = search_model_versions.search(filter=filter, unity_catalog=unity_catalog)
        st.write(f"Retrieved {len(versions)} model versions at {now()}")
        st.session_state.versions = versions
        return versions

    st.subheader("_Model Versions_")

    unity_catalog = st.toggle("Unity Catalog", key="use_uc_model_versions")
    help = """
See [MlflowClient.search_model_versions()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_model_versions). Example: _name='llama'_ or _name like '%viscacha%'_.
"""
    filter = st.text_input("Search filter", key="version_filter", help=help)

    versions = st.session_state.versions if "versions" in st.session_state else []
    if st.button("Refresh", key="refresh_model_versions"):
        versions = refresh(filter, unity_catalog)

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if versions:
        with tab_table:
            df = search_model_versions.as_pandas_df(versions)
            st.write(df)
        with tab_json:
            st.write(versions)

def do_experiments():
    def refresh(filter):
        filter = filter or None
        experiments = search_experiments.search(filter=filter)
        st.write(f"Retrieved {len(experiments)} experiments at {now()}")
        st.session_state.experiments = experiments
        return experiments

    st.subheader("_Experiments_")

    help = """
See [MlflowClient.search_experiments()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_experiments). Example: _name='sklearn_wine'_ or _name like '%sklearn%'_.
"""
    filter = st.text_input("Search filter", key="experiment_filter", help=help)

    experiments = st.session_state.experiments if "experiments" in st.session_state else []
    if st.button("Refresh", key="refresh_experiments"):
        experiments = refresh(filter)

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if experiments:
        with tab_table:
            df = search_experiments.as_pandas_df(experiments)
            st.write(df)
        with tab_json:
            st.write(experiments)


def do_runs():
    from mlflow_reports.list import search_runs
    from mlflow_reports.common import mlflow_utils

    def refresh(exp_id_or_name, filter):
        runs = search_runs.search(exp_id_or_name, filter)
        st.write(f"Retrieved {len(runs)} runs at {now()}")
        exp = mlflow_utils.get_experiment(exp_id_or_name)
        st.write(f"Experiment name: {exp['name']}")
        st.write(f"Experiment ID: {exp['experiment_id']}")
        st.session_state.runs = runs
        return runs

    st.subheader("_Runs_")

    help = """ See [MlflowClient.search_runs()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_runs) """
    exp_id_or_name = st.text_input("Experiment ID or name", "")
    filter = st.text_input("Search filter", key="run_filter", help=help)

    runs = st.session_state.runs if "runs" in st.session_state else []
    if st.button("Refresh", key="refresh_runs"):
        runs = refresh(exp_id_or_name, filter)

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if runs:
        with tab_table:
            df = search_runs.as_pandas_df(runs)
            st.write(df)
        with tab_json:
            st.write(runs)


# ==============
# Object Details

def do_tab_details(raw):
    tab_model, tab_version, tab_experiment, tab_run = \
        st.tabs(["Registered model", "Model version", "Experiment", "Run" ])

    with tab_model:
        do_registered_model(raw)
    with tab_version:
        do_model_version(raw)
    with tab_experiment:
        do_experiment(raw)
    with tab_run:
        do_run(raw)


def do_registered_model(get_raw):
    def refresh(name):
        model = get_registered_model.get(name, get_raw=get_raw)
        st.write(f"Retrieved registered model '{name}' at {now()}")
        st.session_state.model = model
        return model

    model = st.session_state.model if "model" in st.session_state else None
    st.subheader("_Registered Model_")

    help = """
See [MlflowClient.get_registered_model()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_registered_model)."
"""
    model_name = st.text_input("Registered model", key="registered_model", help=help)

    if st.button("Refresh", key="refresh_registered_model"):
        model = refresh(model_name)

    st.write(model)


def do_model_version(get_raw):
    def refresh(name, version):
        vr = get_model_version.get(name, version, get_raw=get_raw)

        model_uri = f"models:/{name}/{version}"
        mlmodel = get_model_artifact(model_uri, "MLmodel", file_type="yaml", explode_json=False)

        signature = copy.deepcopy(mlmodel.get("signature"))
        explode_utils.explode_json(signature)
        st.write(f"Retrieved model version '{name}/{version}' at {now()}")
        st.session_state.version = vr
        return vr, signature, mlmodel

    vr = st.session_state.version if "version" in st.session_state else None
    mlmodel = st.session_state.mlmodel if "mlmodel" in st.session_state else None
    signature = None
    st.header("Model Version")

    help = """
See [MlflowClient.get_model_version()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_model_version)."
"""
    name = st.text_input("Name", key="registered_model_vr", help=help)
    version = st.text_input("Version", key="version_vr", help=help)

    if st.button("Refresh", key="refresh_model_version"):
        vr, signature, mlmodel = refresh(name, version)

    tab_version, tab_signature, tab_mlmodel = st.tabs(["Version", "Signature", "MLmodel"])
    if vr:
        with tab_version:
            st.write(vr)
        with tab_signature:
            st.write(signature)
        with tab_mlmodel:
            st.write(mlmodel)


def do_experiment(get_raw):
    def refresh(name):
        exp = get_experiment.get(name, get_raw=get_raw)
        st.write(f"Retrieved experiment '{name}' at {now()}")
        st.session_state.experiment = exp
        return exp

    experiment = st.session_state.experiment if "experiment" in st.session_state else None
    st.header("Experiment")

    help = """
See [MlflowClient.get_experiment()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_experiment)."
"""
    name = st.text_input("Name", key="experiment_name", help=help)

    if st.button("Refresh", key="refresh_experiment"):
        experiment = refresh(name)

    st.write(experiment)


def do_run(get_raw):
    def refresh(run_id):
        run = get_run.get(run_id, get_raw=get_raw)
        st.write(f"Retrieved run '{run_id}' at {now()}")
        st.session_state.run = run
        return run

    run = st.session_state.run if "run" in st.session_state else None
    st.header("Run")

    help = """
See [MlflowClient.get_run()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_run)."
"""
    name = st.text_input("Run ID", key="run_id", help=help)

    if st.button("Refresh", key="refresh_run"):
        run = refresh(name)

    st.write(run)

if __name__ == "__main__":
    main()

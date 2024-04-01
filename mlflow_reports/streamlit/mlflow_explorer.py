import copy
import streamlit as st
from mlflow.utils.time import Timer
from mlflow_reports.list import search_registered_models, search_model_versions, search_experiments
from mlflow_reports.data import get_registered_model, get_model_version, get_experiment, get_run
from mlflow_reports.mlflow_model.mlflow_model_utils import get_model_artifact
from mlflow_reports.common import explode_utils
from mlflow_reports.common.timestamp_utils import now
from mlflow_reports.client import mlflow_client

from mlflow_reports.streamlit.widgets import (
    init_widgets,
    mk_csv_json_tabs,
    mk_text_input,
    mk_download_button_json,
    mk_download_buttons,
    mk_uc_toggle,
    show_list_msg
)

init_widgets()


def main():
    help="Explore MLlflow objects - registered models, model versions, model signatures, experiments and runs"
    st.title("MLflow API Explorer", help=help)

    st.write(f"MLflow tracking server: {mlflow_client}")

    help = "Add additional fields such as readable timestamps and related objects response JSON"
    raw = not st.checkbox("Enrich response", value=True, key="enrich", help=help)

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
        with Timer() as timer:
            models = search_registered_models.search(filter=filter, unity_catalog=unity_catalog)
        show_list_msg(models, "registered models", timer)
        st.session_state.models = models
        return models

    st.subheader("_Registered Models_")
    unity_catalog = mk_uc_toggle("models_uc")

    help = """
See [MlflowClient.search_registered_models()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_registered_models). Example: _name='sklearn_wine'_ or _name like '%sklearn%'_.
"""
    filter = mk_text_input("Search filter", "model_filter", help=help)

    models = st.session_state.models if "models" in st.session_state else []
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Refresh", key="refresh_registered_models"):
            models = refresh(filter, unity_catalog)
    mk_download_buttons(models, "registered_models", search_registered_models.as_pandas_df, col2, col3)

    mk_csv_json_tabs(models, search_registered_models.as_pandas_df)


def do_model_versions():
    def refresh(filter, unity_catalog):
        filter = filter or None
        with Timer() as timer:
            versions = search_model_versions.search(filter=filter, unity_catalog=unity_catalog)
        show_list_msg(versions, "model versions", timer)
        st.session_state.versions = versions
        return versions


    st.subheader("_Model Versions_")
    unity_catalog = mk_uc_toggle("versions_uc")

    help = """
See [MlflowClient.search_model_versions()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_model_versions). Example: _name='llama'_ or _name like '%viscacha%'_.
"""
    filter = mk_text_input("Search filter", "version_filter", help=help)

    versions = st.session_state.versions if "versions" in st.session_state else []
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Refresh", key="refresh_model_versions"):
            versions = refresh(filter, unity_catalog)
    mk_download_buttons(versions, "model_versions", search_model_versions.as_pandas_df, col2, col3)

    mk_csv_json_tabs(versions, search_model_versions.as_pandas_df)


def do_experiments():
    def refresh(filter):
        filter = filter or None
        with Timer() as timer:
            experiments = search_experiments.search(filter=filter)
        show_list_msg(experiments, "experiments", timer)
        st.session_state.experiments = experiments
        return experiments

    st.subheader("_Experiments_")

    help = """
See [MlflowClient.search_experiments()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_experiments). Example: _name='sklearn_wine'_ or _name like '%sklearn%'_.
"""
    filter = mk_text_input("Search filter", "experiment_filter", help=help)

    experiments = st.session_state.experiments if "experiments" in st.session_state else []
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Refresh", key="refresh_experiments"):
            experiments = refresh(filter)
    mk_download_buttons(experiments, "experiments", search_experiments.as_pandas_df, col2, col3)

    mk_csv_json_tabs(experiments, search_experiments.as_pandas_df)


def do_runs():
    from mlflow_reports.list import search_runs
    from mlflow_reports.common import mlflow_utils

    def refresh(exp_id_or_name, filter):
        with Timer() as timer:
            runs = search_runs.search(exp_id_or_name, filter)
        show_list_msg(runs, "runs", timer)
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
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Refresh", key="refresh_runs"):
            runs = refresh(exp_id_or_name, filter)
    mk_download_buttons(runs, "runs", search_runs.as_pandas_df, col2, col3)

    mk_csv_json_tabs(runs, search_runs.as_pandas_df)


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
    model_name = mk_text_input("Name", "registered_model", help=help)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Refresh", key="refresh_registered_model"):
            model = refresh(model_name)
    with col2:
        mk_download_button_json(model, "registered_model.json", "Download")

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
        return vr, mlmodel, signature

    help = """
See [MlflowClient.get_model_version()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_model_version)."
"""
    st.subheader("_Model Version_", help=help)

    vr = st.session_state.version if "version" in st.session_state else None
    mlmodel = st.session_state.mlmodel if "mlmodel" in st.session_state else None
    signature = st.session_state.signature if "signature" in st.session_state else None

    name = mk_text_input("Name", "registered_model_vr") # , help=help)
    version = mk_text_input("Version", "version_vr")

    col1, col2, col3, col4  = st.columns([1, 1, 1, 1])
    with col1:
        if st.button("Refresh", key="refresh_model_version"):
            vr, mlmodel, signature = refresh(name, version)
    with col2:
        mk_download_button_json(vr, "model_version.json", "Download version")
    with col3:
        mk_download_button_json(mlmodel, "MLmodel.json", "Download MLmodel")
    with col4:
        mk_download_button_json(signature, "signature.json", "Download signature")

    tab_version, tab_mlmodel, tab_signature = st.tabs(["Version", "MLmodel", "Signature"])
    if vr:
        with tab_version:
            st.write(vr)
        with tab_mlmodel:
            st.write(mlmodel)
        with tab_signature:
            st.write(signature)


def do_experiment(get_raw):
    def refresh(name):
        exp = get_experiment.get(name, get_raw=get_raw)
        st.write(f"Retrieved experiment '{name}' at {now()}")
        st.session_state.experiment = exp
        return exp

    experiment = st.session_state.experiment if "experiment" in st.session_state else None
    st.subheader("_Experiment_")

    help = """
See [MlflowClient.get_experiment()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_experiment)."
"""
    name = mk_text_input("Name", "experiment_name", help=help)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Refresh", key="refresh_experiment"):
            experiment = refresh(name)
    with col2:
        mk_download_button_json(experiment, "experiment.json", "Download")

    st.write(experiment)


def do_run(get_raw):
    def refresh(run_id):
        run = get_run.get(run_id, get_raw=get_raw)
        st.write(f"Retrieved run '{run_id}' at {now()}")
        st.session_state.run = run
        return run

    run = st.session_state.run if "run" in st.session_state else None
    st.subheader("_Run_")

    help = """
See [MlflowClient.get_run()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_run)."
"""
    name = mk_text_input("Run ID", "run_id", help=help)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Refresh", key="refresh_run"):
            run = refresh(name)
    with col2:
        mk_download_button_json(run, "run.json", "Download")

    st.write(run)


if __name__ == "__main__":
    main()

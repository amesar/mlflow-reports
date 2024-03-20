import streamlit as st

from mlflow_reports.list import search_registered_models, search_model_versions, search_experiments
from mlflow_reports.common.timestamp_utils import now
from mlflow_reports.client import mlflow_client
#from mlflow_reports.streamlit.unity_catalog.py import do_unity_catalog


def main():
    st.title("List MLflow Objects")
    st.write(f"MLflow tracking server: {mlflow_client}")

    tab_models, tab_versions, tab_experiments, tab_runs = \
        st.tabs(["Registered models", "Model versions", "Experiments", "Runs" ])
    #tab_models, tab_versions, tab_experiments, tab_runs, tab_unity_catalog = \
        #st.tabs(["Registered models", "Model versions", "Experiments", "Runs", "Unity Catalog"])

    with tab_models:
        do_registered_models()
    with tab_versions:
        do_model_versions()
    with tab_experiments:
        do_experiments()
    with tab_runs:
        do_runs()
    #with tab_unity_catalog:
        #do_unity_catalog()


def do_registered_models():
    def refresh(filter, unity_catalog):
        filter = filter or None
        models = search_registered_models.search(filter=filter, unity_catalog=unity_catalog)
        st.write(f"Retrieved {len(models)} registered models at {now()}")
        st.session_state.models = models
        return models

    models = st.session_state.models if "models" in st.session_state else []
    st.header("Registered Models")

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

    st.header("Model Versions")

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

    st.header("Experiments")

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

    st.header("Runs")

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


if __name__ == "__main__":
    main()

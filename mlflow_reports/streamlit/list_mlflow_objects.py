import streamlit as st

from mlflow_reports.list import search_registered_models, search_model_versions, search_experiments
from mlflow_reports.common.timestamp_utils import now
from mlflow_reports.client import mlflow_client


def main():
    st.title("List MLflow Objects")
    st.write(f"MLflow tracking server: {mlflow_client}")

    tab_models, tab_versions, tab_experiments, tab_runs = \
        st.tabs(["Registered models", "Model versions", "Experiments", "Runs"])

    with tab_models:
        do_registered_models()

    with tab_versions:
        do_model_versions()

    with tab_experiments:
        do_experiments()

    with tab_runs:
        do_runs()


def do_registered_models():
    def refresh(unity_catalog):
        models = search_registered_models.search(unity_catalog=unity_catalog)
        st.write(f"Retrieved {len(models)} registered models at {now()}")
        df = search_registered_models.as_pandas_df(models)
        st.dataframe(df) 

    st.header("Registered Models")

    unity_catalog = False
    use_uc = st.toggle("Unity Catalog", key="use_uc_registered_models")
    if use_uc:
        unity_catalog = True

    if st.button("Refresh", key="refresh_registered_models"):
        refresh(unity_catalog)


def do_model_versions():
    def refresh(model_name, unity_catalog):
        filter = f"name='{model_name}'" if model_name else None
        versions = search_model_versions.search(filter=filter, unity_catalog=unity_catalog)
        st.write(f"Retrieved {len(versions)} model versions at {now()}")
        df = search_model_versions.as_pandas_df(versions)
        st.dataframe(df) 
    st.header("Model Versions")

    unity_catalog = False
    use_uc = st.toggle("Unity Catalog", key="use_uc_model_versions")
    if use_uc:
        unity_catalog = True

    model_name = st.text_input(
        "Registered model name (if blank retrieves all model versions which can take a long time)",
        "andre_catalog.ml_models2.sklearn_wine_best",
        key="model_name"
    )
    if st.button("Refresh", key="refresh_model_versions"):
        refresh(model_name, unity_catalog)


def do_experiments():
    def refresh():
        experiments = search_experiments.search()
        st.write(f"Retrieved {len(experiments)} experiments at {now()}")
        df = search_experiments.as_pandas_df(experiments)
        st.dataframe(df) 
    st.header("Experiments")
    if st.button("Refresh", key="refresh_experiments"):
        refresh()


def do_runs():
    def refresh(experiment):
        st.write(f"Experiment: {experiment}")
    st.header("Runs - Coming eventually")
    experiment = st.text_input("Experiment ID or name", "")
    if st.button("Refresh", key="refresh_runs"):
        refresh(experiment)


if __name__ == "__main__":
    main()

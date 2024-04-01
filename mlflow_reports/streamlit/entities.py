import streamlit as st
from mlflow.utils.time import Timer
from mlflow_reports.streamlit.widgets import show_list_msg
from mlflow_reports.streamlit.endpoint_entity import do_model_serving_endpoint_entity as do_details
from mlflow_reports.endpoints import get_endpoints, as_pandas_df
from mlflow_reports.endpoints.list_entities_by_type import (
    mk_all_entities,
    mk_custom_models,
    mk_foundation_models,
    mk_external_models
)


def do_endpoint_entities():
    help = "Entitites == Models"
    st.subheader("_Endpoint entities (models)_", help=help)

    tab_all, tab_custom, tab_foundation, tab_external, tab_details = st.tabs([
        "All models",
        "Custom models",
        "Foundation models",
        "External models",
        "Model details"
    ])


    with tab_all:
        do_tab_all()
    with tab_custom:
        do_tab_custom()
    with tab_foundation:
        do_foundation()
    with tab_external:
        do_tab_external()
    with tab_details:
        do_details()


def do_tab_all():
    def refresh():
        with Timer() as timer:
            endpoints = get_endpoints()
            entities = mk_all_entities(endpoints)
        show_list_msg(entities, "all models", timer)
        st.session_state.all_entities = entities
        return entities

    entities = st.session_state.all_entities if "all_entities" in st.session_state else []

    if st.button("Refresh", key="refresh_endpoints_ent"):
        entities = refresh()

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if entities:
        with tab_table:
            df = as_pandas_df(entities)
            df.sort_values(by=["ep_name", "name"], inplace=True)
            st.write(df)
        with tab_json:
            st.write(entities)


def do_tab_custom():
    class state():
        def set(self, val):
            st.session_state.custom_entities = val
        def get(self, ):
            return st.session_state.custom_entities if "custom_entities" in st.session_state else []
    _do_tab("custom", mk_custom_models, state())


def do_foundation():
    class state():
        def set(self, val):
            st.session_state.foundation_entities = val
        def get(self, ):
            return st.session_state.foundation_entities if "foundation_entities" in st.session_state else []
    _do_tab("foundation", mk_foundation_models, state())


def do_tab_external():
    class state():
        def set(self, val):
            st.session_state.external_entities = val
        def get(self, ):
            return st.session_state.external_entities if "external_entities" in st.session_state else []
    _do_tab("external", mk_external_models, state())


def _do_tab(name, mk_func, session_cls):
    def refresh():
        with Timer() as timer:
            endpoints = get_endpoints()
            entities = mk_func(endpoints)
        show_list_msg(entities, f"{name} models", timer)
        session_cls.set(entities)
        return entities
    entities = session_cls.get()

    key = f"refresh_endpoints_ent_{name}"
    if st.button("Refresh", key=key):
        entities = refresh()

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if entities:
        with tab_table:
            df = as_pandas_df(entities)
            st.write(df)
        with tab_json:
            st.write(entities)

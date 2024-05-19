import streamlit as st
from mlflow.utils.time import Timer

from mlflow_reports.client import databricks_client
from mlflow_reports.common.timestamp_utils import now
from mlflow_reports.streamlit.entities import do_endpoint_entities
from mlflow_reports.model_serving.list_entities_by_type import mk_all_entities
from mlflow_reports.streamlit.widgets import init_widgets, show_list_msg

init_widgets()


def main():
    st.title("Databricks API Explorer", help="Explore Databricks model serving and vector search endpoints")
    st.write(f"Databricks API: {databricks_client}")

    tab_model_serving, tab_vector_search = st.tabs([ "Model serving endpoints", "Vector search endpoints" ] )
    with tab_model_serving:
        do_model_serving()
    with tab_vector_search:
        do_vector_search()


# ==============
# Model serving

def do_model_serving():
    st.header("Model serving endpoints")

    tab_list_endpoints, tab_list_endpoint_details, tab_endpoint, tab_entities = st.tabs([
        "List endpoints",
        "List endpoint details",
        "Endpoint details",
        "Entities"
    ])

    with tab_list_endpoints:
        do_list_model_serving_endpoints()
    with tab_list_endpoint_details:
        do_tab_list_endpoint_details()
    with tab_endpoint:
        do_model_serving_endpoint_details()
    with tab_entities:
        do_endpoint_entities()


def do_list_model_serving_endpoints():
    from mlflow_reports.model_serving import get_endpoints , as_pandas_df
    def refresh():
        with Timer() as timer:
            endpoints = get_endpoints()
        show_list_msg(endpoints, "model serving endpoints", timer)
        st.session_state.list_endpoint_details = endpoints
        return endpoints

    endpoints = st.session_state.list_endpoint_details if "list_endpoint_details" in st.session_state else []
    st.subheader("_List endpoints_")

    if st.button("Refresh", key="refresh_list_endpoint_details"):
        endpoints = refresh()

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if endpoints:
        with tab_table:
            df = as_pandas_df(endpoints)
            df.sort_values(by=["name"], inplace=True)
            st.write(df)
        with tab_json:
            st.write(endpoints)


def do_tab_list_endpoint_details():
    from mlflow_reports.model_serving import get_endpoints , as_pandas_df
    def refresh():
        with Timer() as timer:
            endpoints = get_endpoints() # TODO details
        show_list_msg(endpoints, "model serving endpoint details", timer)
        st.session_state.endpoints = endpoints
        return endpoints

    endpoints = st.session_state.endpoints if "endpoints" in st.session_state else []
    st.subheader("_List endpoint details_")

    if st.button("Refresh", key="refresh_endpoints"):
        endpoints = refresh()

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if endpoints:
        entities = mk_all_entities(endpoints)
        with tab_table:
            df = as_pandas_df(entities)
            df.sort_values(by=["ep_name", "name"], inplace=True)
            st.write(df)
        with tab_json:
            st.write(entities)


def do_model_serving_endpoint_details():
    from mlflow_reports.model_serving import get_endpoint
    def refresh(name):
        if not name:
            return { "error": "Missing model serving endpoint name" }
        endpoint = get_endpoint.get(name)
        st.write(f"Retrieved endpoint _{name}_ at {now()}")
        st.session_state.endpoint = endpoint
        return endpoint

    endpoint = st.session_state.endpoint if "endpoint" in st.session_state else None
    st.subheader("_Endpoint details_")

    name = st.text_input("Endpoint", key="endpoint_name")

    if st.button("Refresh", key="refresh_model_endpoint"):
        endpoint = refresh(name)

    st.write(endpoint)


# ==============
# Vector search

def do_vector_search():
    st.header("Vector search endpoints")
    tab_list_endpoints, tab_endpoint = st.tabs(["List endpoints", "Endpoint details"])

    with tab_list_endpoints:
        do_list_vector_search_endpoints()
    with tab_endpoint:
        do_vector_search_endpoint_details()


def do_list_vector_search_endpoints():
    from mlflow_reports.vector_search.list_endpoints import list, as_pandas_df
    def refresh():
        vs_endpoints = list()
        st.write(f"Retrieved {len(vs_endpoints)} vector search endpoints at {now()}.")
        st.session_state.vs_endpoints = vs_endpoints
        return vs_endpoints

    vs_endpoints = st.session_state.vs_endpoints if "vs_endpoints" in st.session_state else []
    st.subheader("_List endpoints_")

    if st.button("Refresh", key="refresh_vs_endpoints"):
        vs_endpoints = refresh()

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if vs_endpoints:
        with tab_json:
            st.write(vs_endpoints)
        with tab_table:
            df = as_pandas_df(vs_endpoints)
            st.write(df)


def do_vector_search_endpoint_details():
    from mlflow_reports.vector_search import get_endpoint
    def refresh(name):
        if not name:
            #return { "error": "Missing vector search endpoint name" }
            return "ERROR: Missing vector search endpoint name"
        endpoint = get_endpoint.get(name, False)
        st.write(f"Retrieved vector search endpoint '{name}' at {now()}")
        st.session_state.vs_endpoint = endpoint
        return endpoint

    endpoint = st.session_state.vs_endpoint if "vs_endpoint" in st.session_state else None
    st.subheader("_Endpoint details_")

    name = st.text_input("Endpoint", key="vs_endpoint_name")

    if st.button("Refresh", key="refresh_vs_model_endpoint"):
        endpoint = refresh(name)

    st.write(endpoint)


if __name__ == "__main__":
    main()

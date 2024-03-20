import streamlit as st
from mlflow_reports.common.timestamp_utils import now


def main():
    st.title("Databricks Endpoints")

    from mlflow_reports.client.http_client import dbx_20_client
    st.write(f"API: {dbx_20_client}")

    tab_model_serving_endpoints, tab_vector_search_endpoints, tab_vector_search_indexes = \
      st.tabs(["Model Serving Endpoints", "Vector Search Endpoints", "Vector Search Indexes" ])

    with tab_model_serving_endpoints:
        do_model_serving_endpoints()

    with tab_vector_search_endpoints:
        do_vector_search_endpoints()

    with tab_vector_search_indexes:
        do_vector_search_indexes()


def do_model_serving_endpoints():
    from mlflow_reports.endpoints import get_endpoints, as_pandas_df
    def refresh():
        endpoints = get_endpoints()
        st.write(f"Retrieved {len(endpoints)} model serving endpoints at {now()}.")
        st.session_state.endpoints = endpoints
        return endpoints

    endpoints = st.session_state.endpoints if "endpoints" in st.session_state else []
    st.header("Model Serving Endpoints")

    if st.button("Refresh", key="refresh_endpoints"):
        endpoints = refresh()

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if endpoints:
        with tab_table:
            df = as_pandas_df(endpoints)
            df.sort_values(by=["name"], inplace=True)
            st.write(df)
        with tab_json:
            st.write(endpoints)


def do_vector_search_endpoints():
    from mlflow_reports.vector_search.list_endpoints import list_endpoints, as_pandas_df
    def refresh():
        vs_endpoints = list_endpoints()
        st.write(f"Retrieved {len(vs_endpoints)} vector search endpoints at {now()}.")
        st.session_state.vs_endpoints = vs_endpoints
        return vs_endpoints

    vs_endpoints = st.session_state.vs_endpoints if "vs_endpoints" in st.session_state else []
    st.header("Vector Search Endpoints")

    if st.button("Refresh", key="refresh_vs_endpoints"):
        vs_endpoints = refresh()

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if vs_endpoints:
        with tab_json:
            st.write(vs_endpoints)
        with tab_table:
            df = as_pandas_df(vs_endpoints)
            st.write(df)


def do_vector_search_indexes():
    from mlflow_reports.vector_search.list_indexes import list_indexes, as_pandas_df
    def refresh(vs_endpoint):
        vs_indexes = list_indexes(vs_endpoint)
        st.write(f"Retrieved {len(vs_indexes)} vector search indexes for endpoint '{vs_endpoint}' at {now()}.")
        st.session_state.vs_indexes = vs_indexes
        return vs_indexes

    vs_indexes = st.session_state.vs_indexes if "vs_indexes" in st.session_state else []
    st.header("Vector Search Indexes")

    vs_endpoint = st.text_input("Vector Search endpoint", key="vs_endpoint") # , help=)

    if st.button("Refresh", key="refresh_vs_indexes"):
        vs_indexes = refresh(vs_endpoint)

    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if vs_indexes:
        with tab_json:
            st.write(vs_indexes)
        with tab_table:
            df = as_pandas_df(vs_indexes)
            st.write(df)


if __name__ == "__main__":
    main()

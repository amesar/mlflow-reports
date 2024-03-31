import json
import streamlit as st
from mlflow_reports.common import mlflow_utils


def init_widgets():
    css = """
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:18px;
    }
    button.css {
        border: 2px solid #000000;
    }

    div[data-testid="column"] {
        width: fit-content !important;
        flex: unset;
    }
    div[data-testid="column"] * {
        width: fit-content !important;
    }
</style>
"""
    st.markdown(css, unsafe_allow_html=True)


def mk_text_input(name, key, help=None):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.write("##")
        st.write(name)
    with col2:
        val = st.text_input("", key=key, help=help)
    return val


def mk_download_button_csv(df, file_name):
    st.download_button(
        label="Download as CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name=file_name,
        mime='text/csv',
    )


def mk_download_button_json(data, file_name, label="Download as JSON"):
    st.download_button(
        label=label,
        data=json.dumps(data, indent=2),
        file_name=file_name,
        mime='application/json',
    )


def mk_download_buttons(data, file_name_base, to_pandas_df_func, col_download_csv, col_download_json):
    with col_download_csv:
        df = to_pandas_df_func(data)
        mk_download_button_csv(df, f"{file_name_base}.csv")
    with col_download_json:
        mk_download_button_json(data, f"{file_name_base}.json")


def mk_csv_json_tabs(data, to_pandas_df_func):
    tab_table, tab_json = st.tabs(["Table", "JSON"])
    if data:
        with tab_table:
            df = to_pandas_df_func(data)
            st.write(df)
        with tab_json:
            st.write(data)


def mk_uc_toggle(key):
    if mlflow_utils.is_calling_databricks():
    #if True:
        help = "Default is Unity Catalog Model Registry"
        use_ws = st.checkbox("Use Workspace Model Registry", key=key, help=help)
        return not use_ws
    else:
        return False

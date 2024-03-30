import streamlit as st

def init_widgets():
    css = """
<style>
  .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:18px;
  }
  button.css {
    border: 2px solid #000000;
  }
</style>
"""
    st.markdown(css, unsafe_allow_html=True)


def mk_text_input(name, key, help=None):
    c1, c2 = st.columns([1, 4])
    with c1:
        st.write("##")
        st.write(name)
    with c2:
        val = st.text_input("", key=key, help=help)
    return val

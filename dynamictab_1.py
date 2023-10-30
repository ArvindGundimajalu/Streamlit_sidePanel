import itertools

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit Theme for Charts", page_icon="🗃")

st.title("Tab Container Prototype")

@st.experimental_memo
def get_data():
    return pd.DataFrame(np.random.randn(20, 5), columns=["a", "b", "c", "d", "e"])

if "tabs" not in st.session_state:
    st.session_state["tabs"] = ["Filter Data", "Raw Data", "📈 Chart"]

if "tabs_sidebar" not in st.session_state:
    st.session_state["tabs_sidebar"] = False

tabs = st.tabs(st.session_state["tabs"])

with tabs[0]:
    col = st.selectbox("Select column", options=["a", "b", "c"])
    filter = st.slider("Filter range", -2.5, 2.5, (-2.0, 2.0), step=0.01)
    filter_query = f"{filter[0]} < {col} < {filter[1]}"

with tabs[1]:
    st.dataframe(get_data().query(filter_query), height=300)

with tabs[2]:
    st.line_chart(get_data().query(filter_query))

new_tab = st.text_input("Tab label", "New Tab")
if st.button("Add tab"):
    st.empty()
    st.session_state["tabs"].append(new_tab)
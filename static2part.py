import itertools

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit Theme for Charts", page_icon="🗃")


st.title("Tab Container Prototype")

tabCount = 1

@st.cache_data
def get_data():
    return pd.DataFrame(np.random.randn(20, 5), columns=["a", "b", "c", "d", "e"])

if "tabs" not in st.session_state:
    st.session_state["tabs"] = ["Chat", "Details"]

tabs = st.tabs(st.session_state["tabs"])

with tabs[0]:
    tabs[0].write("hello world")

with tabs[1]:
    tabs[1].write("bla bla bla")

new_tab = st.text_input("Tab label", "New Tab")
if st.button("Add tab"):
    tabs = st.empty()
    st.session_state["tabs"].append(new_tab)
    tabs = st.tabs(st.session_state["tabs"])
    tabCount += 1
    tabs[tabCount].write("Arvind")
import itertools

import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_data():
    return pd.DataFrame(np.random.randn(20, 5), columns=["a", "b", "c", "d", "e"])

if "tabs" not in st.session_state:
    st.session_state["tabs"] = ["Chat"]

tabs = st.tabs(st.session_state["tabs"])

with tabs[0]:
    col = st.selectbox("Select column", options=["a", "b", "c"])
    filter = st.slider("Filter range", -2.5, 2.5, (-2.0, 2.0), step=0.01)
    filter_query = f"{filter[0]} < {col} < {filter[1]}"

st.session_state["tabs"].append("Olive Garden")
tabs = st.tabs(st.session_state["tabs"])
with tabs[1]:
    st.dataframe(get_data().query(filter_query), height=300)

st.session_state["tabs"].append("Chinnar")
del tabs

tabs = st.tabs(st.session_state["tabs"])
with tabs[2]:
    st.dataframe(get_data().query(filter_query), height=300)
    st.experimental_rerun()
#st.markdown("Tabs Configruations")
#
#entityName = "Welcome"
#new_tab = st.text_input("Tab label", entityName)
#if st.button("Add tab"):
#    st.session_state["tabs"].append(new_tab)
#    tabs = st.tabs(st.session_state["tabs"])
#    with tabs[3]:
#        st.title("A dog")
#        st.markdown("#bla bla bla")

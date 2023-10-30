import streamlit as st


# page config
st.set_page_config(layout="wide")

# split window into 2 column-wise sections
#     one for options, one for content
options_col, content_col = st.columns([2, 5], gap="large")

with options_col:
    # model options
    model_selection = st.selectbox('Model', ["Test 1", "Test 2"], key="model_selection")
    # dynamic filters
    filter_container = st.empty()

with content_col:
    if model_selection == "Test 1":
        st.markdown("## Test 1 Model")

        # list tabs
        test1_tab1, test1_tab2 = st.tabs(["Test 1 Tab 1", "Test 1 Tab 2"])
        with test1_tab1:
            with filter_container:
                test1_tab1_selectbox = st.selectbox('Test 1 Tab 1 Selectbox', ['Test 1 Select 1', 'Test 1 Select 2'],
                    key="test1_tab1_selectbox")

        with test1_tab2:
            with filter_container:
                test1_tab2_selectbox = st.selectbox('Test 1 Tab 2 Selectbox', ['Test 1 Select 1'],
                    key="test1_tab2_selectbox")

    elif model_selection == "Test 2":
        st.markdown("## Test 2 Model")

        # list tabs
        tabs = st.tabs(["Test 2 Tab 1"])
        with tabs[0]:
            with filter_container:
                test2_tab1_selectbox = st.selectbox('Test 2 Tab 1 Selectbox', ['Test 2 Select 1', 'Test 2 Select 2'],
                    key="test2_tab1_selectbox")
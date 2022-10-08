# to run this
# open terminal
# enter the commands
# 1.
# cd data_app1
# 2.
# streamlit run app.py

import streamlit as st

st.set_page_config(
    page_title="Data App 1",
    page_icon="😎",
    layout="wide")

st.title("📊 Data Analytics App")
st.info("This is a simple data analytics app")

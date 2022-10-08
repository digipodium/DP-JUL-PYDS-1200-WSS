'''
-> to run this, dont click on play
-> open terminal, enter the commands 1 and 2
-> cd data_app1
-> streamlit run app.py
'''

import streamlit as st
import pandas as pd
import numpy as np  

st.set_page_config(
    page_title="Data App 1",
    page_icon="😎",
    layout="wide")  

st.title("📊 Data Analytics App")
st.info("This is a simple data analytics app")

@st.cache # decorator <- to cache the data
def load_data():
    data = pd.read_csv("cps_85_wages.csv")
    return data

data = load_data()
st.dataframe(data, use_container_width=True)


c1, c2 = st.columns(2)
c1.header("Data Information (numeric)")
c2.header("Data Columns")
if c1.checkbox("View Data Information"):
    c1.dataframe(data.describe(), use_container_width= True)
if c2.checkbox("View Data Columns"):
    c2.dataframe(data.columns, use_container_width= True)

st.header("Data Summary")
c1, c2 = st.columns(2)

numerical_columns = data.select_dtypes(include=np.number).columns
categorical_columns = data.select_dtypes(exclude=np.number).columns
index_col = c1.selectbox("Select Column for Index (categorical)", categorical_columns)
values_col = c1.multiselect("Select Column for Values (numerical)", numerical_columns)
agg_func = c1.selectbox("Select Aggregation Function", ["mean", "sum", "count", "min", "max",'std'])

out = pd.pivot_table(data, index=index_col, values=values_col, aggfunc=agg_func)
c2.dataframe(out,use_container_width=True)
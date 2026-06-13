import streamlit as st
import pandas as pd

st.title("Executive Dashboard")

df = pd.read_csv("dataset/sales_data.csv")

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Sales",
    int(df["sales"].sum())
)

col2.metric(
    "Revenue",
    f"₹{df['revenue'].sum():,.0f}"
)

col3.metric(
    "Products",
    df["product"].nunique()
)

st.dataframe(df)
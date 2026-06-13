import streamlit as st
import pandas as pd

st.title("Upload Dataset")

file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if file:

    df = pd.read_csv(file)

    st.dataframe(df.head())
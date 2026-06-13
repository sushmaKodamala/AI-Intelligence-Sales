import streamlit as st
import pandas as pd

st.title("Data Preprocessing")

try:
    df = pd.read_csv("dataset/sales_data.csv")

    st.subheader("Original Dataset")
    st.dataframe(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(0)

    st.subheader("Processed Dataset")
    st.dataframe(df)

    if st.button("Save Processed Data"):
        df.to_csv(
            "dataset/processed_sales.csv",
            index=False
        )
        st.success("Processed data saved successfully!")

except Exception as e:
    st.error(str(e))
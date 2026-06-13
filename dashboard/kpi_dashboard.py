import streamlit as st

def display_kpis(df):

    total_sales = df["sales"].sum()

    total_revenue = df["revenue"].sum()

    st.metric(
        "Total Sales",
        total_sales
    )

    st.metric(
        "Revenue",
        f"₹{total_revenue:,.2f}"
    )
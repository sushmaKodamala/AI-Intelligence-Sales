import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Exploratory Data Analysis")

try:

    df = pd.read_csv(
        "dataset/sales_data.csv"
    )

    st.dataframe(df.head())

    st.subheader("Dataset Information")

    st.write(df.describe())

    st.subheader("Sales By Product")

    fig1 = px.bar(
        df,
        x="product",
        y="sales",
        color="category"
    )

    st.plotly_chart(fig1)

    st.subheader("Revenue By Product")

    fig2 = px.pie(
        df,
        names="product",
        values="revenue"
    )

    st.plotly_chart(fig2)

    st.subheader("Sales Trend")

    fig3 = px.line(
        df,
        x="date",
        y="sales",
        markers=True
    )

    st.plotly_chart(fig3)

except Exception as e:

    st.error(e)
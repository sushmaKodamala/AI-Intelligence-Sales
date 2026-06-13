import plotly.express as px
import streamlit as st

def sales_chart(df):

    fig = px.line(
        df,
        x="date",
        y="sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
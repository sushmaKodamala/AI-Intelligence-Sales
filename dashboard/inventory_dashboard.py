import streamlit as st

def inventory_summary(stock):

    st.info(
        f"Current Inventory : {stock}"
    )
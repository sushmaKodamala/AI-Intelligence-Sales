import streamlit as st

st.title("Inventory Optimization")

daily_sales = st.number_input(
    "Average Daily Sales",
    value=10
)

lead_time = st.number_input(
    "Lead Time (Days)",
    value=5
)

if st.button("Calculate"):

    reorder_point = (
        daily_sales *
        lead_time
    )

    st.success(
        f"Reorder Point : {reorder_point}"
    )
import streamlit as st
import pandas as pd
import joblib

st.title("Sales Forecasting")

try:

    model = joblib.load(
        "model/sales_forecast_model.pkl"
    )

    sales = st.number_input(
        "Enter Sales Quantity",
        min_value=1,
        value=10
    )

    if st.button("Forecast Revenue"):

        prediction = model.predict(
            [[sales]]
        )

        st.success(
            f"Predicted Revenue: ₹ {prediction[0]:,.2f}"
        )

except Exception as e:

    st.error(e)
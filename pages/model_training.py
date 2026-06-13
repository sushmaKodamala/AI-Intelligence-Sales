import streamlit as st
import os

st.title("Train Model")

if st.button("Train"):

    os.system(
        "python model/train_model.py"
    )

    st.success("Training Completed")
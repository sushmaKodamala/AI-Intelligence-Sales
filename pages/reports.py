import streamlit as st
from reports.generate_pdf_report import generate_report

st.title("Generate Reports")

if st.button("Generate PDF"):

    file = generate_report()

    st.success(
        "PDF Generated Successfully"
    )

    with open(file, "rb") as pdf:

        st.download_button(
            label="Download PDF",
            data=pdf,
            file_name="sales_report.pdf",
            mime="application/pdf"
        )
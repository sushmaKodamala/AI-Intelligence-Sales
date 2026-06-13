from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet

def generate_report():

    doc = SimpleDocTemplate(
        "sales_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Intelligent Sales Forecast Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1,12)
    )

    content.append(
        Paragraph(
            "Sales Forecasting System Generated Report",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return "sales_report.pdf"
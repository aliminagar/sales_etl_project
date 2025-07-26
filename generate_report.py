from fpdf import FPDF
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus

load_dotenv()

# Fetch sales data
def fetch_sales_data():
    user = os.getenv("DB_USER")
    password = quote_plus(os.getenv("DB_PASSWORD"))  # Encode special chars
    host = os.getenv("DB_HOST")
    db = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT", "3306")

    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(connection_string)
    query = "SELECT * FROM sales_data"
    return pd.read_sql(query, engine)

# Generate the PDF
def generate_pdf_report(df):
    df["total_sales"] = df["quantity"] * df["price"]

    total_revenue = df["total_sales"].sum()
    total_orders = len(df)
    unique_customers = df["customer_id"].nunique()

    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Sales Dashboard Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Total Revenue: ${total_revenue:,.2f}", ln=True)
    pdf.cell(0, 10, f"Total Orders: {total_orders}", ln=True)
    pdf.cell(0, 10, f"Unique Customers: {unique_customers}", ln=True)
    pdf.ln(10)

    # Charts
    for chart in ["sales_by_category.png", "sales_by_product.png", "sales_over_time.png"]:
        if os.path.exists(chart):
            pdf.image(chart, x=10, w=180)
            pdf.ln(10)
        else:
            pdf.cell(0, 10, f"[Missing Chart: {chart}]", ln=True)

    # Output
    pdf.output("sales_report.pdf")
    print("PDF report saved as: sales_report.pdf")

# Main
if __name__ == "__main__":
    df = fetch_sales_data()
    generate_pdf_report(df)

from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from sqlalchemy import create_engine
load_dotenv()
# Connect to MySQL and load data into pandas
def fetch_sales_data():
    user = os.getenv("DB_USER")
    raw_password = os.getenv("DB_PASSWORD")  
    password = quote_plus(raw_password)      
    host = os.getenv("DB_HOST")
    db = os.getenv("DB_NAME")

    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{db}"
    engine = create_engine(connection_string)
    query = "SELECT * FROM sales_data"
    df = pd.read_sql(query, engine)
    return df

# Plot total sales by product category
def plot_sales_by_category(df):
    df["total_sales"] = df["quantity"] * df["price"]
    category_summary = df.groupby("category")["total_sales"].sum()
    category_summary.plot(kind="bar", title="Total Sales by Category")
    plt.ylabel("Revenue ($)")
    plt.xlabel("Category")
    plt.tight_layout()
    plt.savefig("sales_by_category.png")
    #plt.show()

# Plot sales trend over time
def plot_sales_over_time(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["total_sales"] = df["quantity"] * df["price"]
    trend = df.groupby("order_date")["total_sales"].sum()
    trend.plot(kind="line", marker='o', title="Sales Over Time")
    plt.ylabel("Revenue ($)")
    plt.xlabel("Order Date")
    plt.tight_layout()
    plt.savefig("sales_over_time.png")
    #plt.show()

# Plot total sales by product
def plot_sales_by_product(df):
    df["total_sales"] = df["quantity"] * df["price"]
    product_summary = df.groupby("product")["total_sales"].sum()
    product_summary.plot(kind="bar", title="Total Sales by Product", color="skyblue")
    plt.ylabel("Revenue ($)")
    plt.xlabel("Product")
    plt.tight_layout()
    plt.savefig("sales_by_product.png")
    #plt.show()

# Show summary stats
def print_summary(df):
    df["total_sales"] = df["quantity"] * df["price"]
    total = df["total_sales"].sum()
    print("\n📊 SALES DASHBOARD\n" + "="*30)
    print(f"💰 Total Revenue: ${total:.2f}")
    print(f"🧾 Total Orders: {len(df)}")
    print(f"🧍 Unique Customers: {df['customer_id'].nunique()}\n")

# Main entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sales Dashboard Visualization")
    parser.add_argument("--plot", choices=["all", "category", "product", "trend"], default="all",
                        help="Choose which chart to display")
    args = parser.parse_args()

    df = fetch_sales_data()
    print_summary(df)

    if args.plot == "all":
        plot_sales_by_category(df)
        plot_sales_over_time(df)
        plot_sales_by_product(df)
    elif args.plot == "category":
        plot_sales_by_category(df)
    elif args.plot == "product":
        plot_sales_by_product(df)
    elif args.plot == "trend":
        plot_sales_over_time(df)
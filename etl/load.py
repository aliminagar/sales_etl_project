import mysql.connector
import pandas as pd
from etl.transform import transform_sales_data

def load_to_mysql(df):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Andrew@Yale2025",  # Your MySQL password
        database="sales_etl"
    )
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO sales_data (
            order_id, customer_id, product, category, quantity, price, order_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, (
    row["order_id"],
    row["customer_id"],
    row["product"],
    row["category"],
    row["quantity"],
    row["price"],
    row["order_date"]
))

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    raw_data = {
        "order_id": [1, 2],
        "customer_id": [101, 102],
        "product": ["Widget", "Gadget"],
        "category": ["A", "B"],
        "quantity": [3, 5],
        "price": [10.0, 20.0],
        "order_date": ["2024-01-01", "2024-01-02"]
    }
    df_raw = pd.DataFrame(raw_data)
    df = transform_sales_data(df_raw)
    load_to_mysql(df)

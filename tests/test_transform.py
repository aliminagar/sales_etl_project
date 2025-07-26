import pandas as pd
from etl.transform import transform_sales_data

def test_transform_sales_data():
    # Mock input data
    data = {
        "order_id": [1, 2],
        "customer_id": [101, 102],
        "product": ["Widget", "Gadget"],
        "category": ["A", "B"],
        "quantity": [3, 5],
        "price": [10.0, 20.0],
        "order_date": ["2024-01-01", "2024-01-02"]
    }
    df = pd.DataFrame(data)

    transformed_df = transform_sales_data(df)

    assert "total_sales" in transformed_df.columns
    assert transformed_df["total_sales"].iloc[0] == 30.0
    assert transformed_df["total_sales"].iloc[1] == 100.0
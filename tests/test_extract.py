# tests/test_extract.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from etl.extract import extract_sales_data

def test_extract_sales_data():
    test_file = "./data/raw_sales_data.csv"
    df = extract_sales_data(test_file)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    
    expected_columns = {"order_id", "customer_id", "product", "category", "quantity", "price", "order_date"}
    assert expected_columns.issubset(df.columns)

    expected_columns = {"order_id", "customer_id", "product", "category", "quantity", "price", "order_date"}
    assert expected_columns.issubset(df.columns)
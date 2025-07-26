import pandas as pd
import os
from etl.load import load_sales_data

def test_load_sales_data(tmp_path):
    # Sample test DataFrame
    df = pd.DataFrame({
        'product': ['A', 'B'],
        'quantity': [2, 3],
        'price': [10.0, 15.0]
    })
    df['total_sales'] = df['quantity'] * df['price']

    # Temporary output file
    output_file = tmp_path / "test_output.csv"
    load_sales_data(df, output_file)

    # Check file exists
    assert output_file.exists()

    # Check contents
    loaded_df = pd.read_csv(output_file)
    assert loaded_df.shape == df.shape
    assert "total_sales" in loaded_df.columns
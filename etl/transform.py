import pandas as pd

def transform_sales_data(df):
    # Drop rows with missing values
    df = df.dropna()

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Convert quantity and price to numeric types
    df["quantity"] = df["quantity"].astype(int)
    df["price"] = df["price"].astype(float)

    # Create total_sales column
    df["total_sales"] = df["quantity"] * df["price"]

    return df

if __name__ == "__main__":
    # Load raw sales data
    df = pd.read_csv("./data/raw_sales_data.csv")

    # Transform the data
    transformed_df = transform_sales_data(df)

    # Show preview
    print(transformed_df.head())

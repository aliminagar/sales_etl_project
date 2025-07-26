import pandas as pd

def extract_sales_data(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    file_path = "./data/raw_sales_data.csv"  
    data = extract_sales_data(file_path)
    print(data.head())
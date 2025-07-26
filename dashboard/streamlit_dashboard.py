import streamlit as st
import pandas as pd
import sqlite3

# Page config
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    """Load data from SQLite database"""
    try:
        conn = sqlite3.connect("data/sales.db")
        df = pd.read_sql("SELECT * FROM sales", conn)
        conn.close()
        return df
    except:
        # Fallback to CSV if database doesn't exist
        return pd.read_csv("data/raw_sales_data.csv")

def main():
    st.title("📊 Sales Analytics Dashboard")
    st.markdown("---")
    
    # Load data
    df = load_data()
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    categories = st.sidebar.multiselect(
        "Select Categories",
        options=df['category'].unique(),
        default=df['category'].unique()
    )
    
    # Filter data
    filtered_df = df[df['category'].isin(categories)]
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sales = filtered_df['price'].sum() if 'price' in filtered_df.columns else filtered_df['total_amount'].sum()
        st.metric("💰 Total Sales", f"${total_sales:,.2f}")
    
    with col2:
        total_orders = len(filtered_df)
        st.metric("📦 Total Orders", f"{total_orders:,}")
    
    with col3:
        avg_order = total_sales / total_orders if total_orders > 0 else 0
        st.metric("📈 Avg Order Value", f"${avg_order:.2f}")
    
    with col4:
        total_products = filtered_df['product'].nunique()
        st.metric("🛍️ Unique Products", total_products)
    
    st.markdown("---")
    
    # Charts row
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Sales by Category")
        price_col = 'price' if 'price' in filtered_df.columns else 'total_amount'
        category_sales = filtered_df.groupby('category')[price_col].sum().reset_index()
        
        st.bar_chart(category_sales.set_index('category'))
    
    with col2:
        st.subheader("📈 Sales by Product")
        product_sales = filtered_df.groupby('product')[price_col].sum().reset_index()
        
        st.bar_chart(product_sales.set_index('product'))
    
    # Data table
    st.subheader("📋 Raw Data")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name='sales_data.csv',
        mime='text/csv'
    )

if __name__ == "__main__":
    main()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv('./db/clean_sales_data.csv')

# Set the style
sns.set(style="whitegrid")

# 🟦 Total Sales by Category
plt.figure(figsize=(8, 5))
category_plot = sns.barplot(data=df, x='category', y='total_sales', estimator=sum, ci=None)
plt.title('Total Sales by Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('dashboard/total_sales_by_category.png')  # 🔹 Save chart
plt.show()

# 🟧 Total Sales by Date
plt.figure(figsize=(8, 5))
date_plot = sns.lineplot(data=df, x='order_date', y='total_sales', marker='o')
plt.title('Total Sales by Date')
plt.xlabel('Order Date')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('dashboard/total_sales_by_date.png')  # 🔹 Save chart
plt.show()

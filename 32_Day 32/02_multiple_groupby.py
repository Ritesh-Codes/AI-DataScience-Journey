import pandas as pd

# Sample dataset: sales records of different regions and products
data = {
    "Region": ["North", "North", "South", "South", "East", "East", "West", "West", "North", "South"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [1200, 800, 1500, 1000, 1100, 700, 1300, 900, 1250, 950],
    "Quantity": [3, 5, 4, 6, 2, 4, 3, 7, 5, 6]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Group by Region and Product, calculate total sales
sales_group = df.groupby(["Region", "Product"])["Sales"].sum()
print("\nTotal Sales by Region and Product:")
print(sales_group)

# 2. Group by Region and Product, calculate average quantity
avg_quantity = df.groupby(["Region", "Product"])["Quantity"].mean()
print("\nAverage Quantity by Region and Product:")
print(avg_quantity)

# 3. Group by Region and Product with multiple aggregations
multi_agg = df.groupby(["Region", "Product"]).agg({
    "Sales": ["sum", "mean"],
    "Quantity": ["sum", "mean"]
})
print("\nMultiple Aggregations (Sales & Quantity):")
print(multi_agg)
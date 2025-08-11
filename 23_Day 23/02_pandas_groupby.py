import pandas as pd

# Create sample sales data
data = {
    "Store": ["A", "B", "A", "B", "A", "C", "C", "B"],
    "Product": ["Apples", "Bananas", "Apples", "Apples", "Bananas", "Bananas", "Apples", "Bananas"],
    "Sales": [100, 150, 120, 90, 200, 130, 140, 180]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Group by store and calculate total sales
store_sales = df.groupby("Store")["Sales"].sum()
print("\nTotal Sales by Store:\n", store_sales)

# Group by product and calculate average sales
product_avg_sales = df.groupby("Product")["Sales"].mean()
print("\nAverage Sales by Product:\n", product_avg_sales)

# Group by store and product
store_product_sales = df.groupby(["Store", "Product"])["Sales"].sum()
print("\nTotal Sales by Store and Product:\n", store_product_sales)

# Save results
store_sales.to_csv("02_store_sales.csv")
product_avg_sales.to_csv("02_product_avg_sales.csv")
store_product_sales.to_csv("02_store_product_sales.csv")
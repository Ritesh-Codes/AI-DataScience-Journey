import pandas as pd

# Create DataFrame
data = {
    "Store": ["A", "A", "B", "B", "C", "C", "A", "B", "C"],
    "Product": ["Apple", "Banana", "Apple", "Banana", "Apple", "Banana", "Apple", "Apple", "Banana"],
    "Sales": [200, 150, 300, 250, 400, 300, 100, 350, 200],
    "Quantity": [20, 15, 30, 25, 40, 30, 10, 35, 20]
}
df = pd.DataFrame(data)
print("Sales Data:\n", df)

# Total Sales by Store
store_sales = df.groupby("Store")["Sales"].sum()
print("\nTotal Sales by Store:\n", store_sales)

# Product Summary: Total Sales & Average Quantity
product_summary = df.groupby("Product").agg({
    "Sales": "sum",
    "Quantity": "mean"
})
print("\nProduct Summary (Total Sales & Avg Quantity):\n", product_summary)

# Multiple Aggregations for Store
store_multi_agg = df.groupby("Store").agg({
    "Sales": ["sum", "mean", "max"],
    "Quantity": ["sum", "mean"]
})
print("\nStore Multiple Aggregations:\n", store_multi_agg)
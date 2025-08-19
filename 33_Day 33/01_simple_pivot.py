import pandas as pd

# Sample sales dataset
data = {
    "Product": ["Laptop", "Laptop", "Phone", "Phone", "Tablet", "Tablet"],
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Sales": [1200, 1500, 800, 900, 400, 500]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Pivot table: total sales by Product
pivot = pd.pivot_table(df, values="Sales", index="Product", aggfunc="sum")

print("\nPivot Table - Total Sales by Product:\n", pivot)
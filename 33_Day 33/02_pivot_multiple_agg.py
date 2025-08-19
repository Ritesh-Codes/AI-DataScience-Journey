import pandas as pd

# Sample sales dataset
data = {
    "Product": ["Laptop", "Laptop", "Phone", "Phone", "Tablet", "Tablet", "Laptop", "Phone"],
    "Region": ["North", "South", "North", "South", "North", "South", "North", "South"],
    "Sales": [1200, 1500, 800, 900, 400, 500, 1300, 950],
    "Quantity": [5, 7, 10, 12, 6, 4, 8, 15]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Pivot table with multiple aggregation functions
pivot = pd.pivot_table(
    df,
    values=["Sales", "Quantity"],
    index="Product",
    aggfunc={"Sales": ["sum", "mean"], "Quantity": ["sum", "mean"]}
)

print("\nPivot Table - Multiple Aggregations:\n", pivot)
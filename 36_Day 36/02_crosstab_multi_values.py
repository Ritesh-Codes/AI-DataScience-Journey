import pandas as pd

# Sample DataFrame
data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Product": ["A", "A", "B", "B", "C", "C", "A", "B"],
    "Sales": [120, 80, 90, 100, 200, 150, 130, 170],
    "Quantity": [10, 7, 5, 8, 15, 12, 9, 11],
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

# Crosstab for Sales
ct_sales = pd.crosstab(
    index=df["Region"],
    columns=df["Product"],
    values=df["Sales"],
    aggfunc="sum",
    margins=True,
    margins_name="Total"
)

# Crosstab for Quantity
ct_quantity = pd.crosstab(
    index=df["Region"],
    columns=df["Product"],
    values=df["Quantity"],
    aggfunc="sum",
    margins=True,
    margins_name="Total"
)

print("Crosstab (Sales):\n", ct_sales, "\n")
print("Crosstab (Quantity):\n", ct_quantity, "\n")

# Optionally merge into MultiIndex columns
combined = pd.concat(
    {"Sales": ct_sales, "Quantity": ct_quantity},
    axis=1
)

print("Combined Crosstab:\n", combined)
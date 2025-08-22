import pandas as pd

# Sample retail dataset
data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West", "North", "South"],
    "Product": ["A", "A", "B", "B", "C", "C", "A", "B", "C", "A"],
    "Sales": [120, 80, 90, 100, 200, 150, 130, 170, 220, 95],
    "Quantity": [10, 7, 5, 8, 15, 12, 9, 11, 16, 6],
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Add a Sales Category column
df["Sales_Category"] = pd.cut(
    df["Sales"],
    bins=[0, 100, 150, 200, 300],
    labels=["Low", "Medium", "High", "Very High"]
)

print("\nDataFrame with Sales Category:\n", df)

# Crosstab: Region vs Sales Category
ct_region_sales = pd.crosstab(
    index=df["Region"],
    columns=df["Sales_Category"],
    margins=True,
    margins_name="Total"
)

print("\nCrosstab: Region vs Sales Category\n", ct_region_sales)

# Crosstab: Product vs Sales Category with normalization
ct_product_sales = pd.crosstab(
    index=df["Product"],
    columns=df["Sales_Category"],
    normalize="index"
)

print("\nCrosstab (Normalized): Product vs Sales Category\n", ct_product_sales.round(2))
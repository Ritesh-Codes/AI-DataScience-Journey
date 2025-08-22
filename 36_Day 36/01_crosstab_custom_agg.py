import pandas as pd
import numpy as np

# Sample dataset
data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Product": ["A", "A", "B", "B", "C", "C", "A", "B"],
    "Sales": [120, 80, 90, 100, 200, 150, 130, 170], 
    "Quantity": [10, 7, 5, 8, 15, 12, 9, 11]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Crosstab with SUM of Sales
ct_sum = pd.crosstab(
    index=df["Region"],
    columns=df["Product"],
    values=df["Sales"],
    aggfunc=np.sum,
    margins=True,
    margins_name="Total"
)
print("\nCrosstab: SUM of Sales")
print(ct_sum)

# Crosstab with MEAN of Sales
ct_mean = pd.crosstab(
    index=df["Region"],
    columns=df["Product"],
    values=df["Sales"],
    aggfunc=np.mean,
    margins=True
)
print("\nCrosstab: MEAN of Sales")
print(ct_mean)

# Crosstab with MULTIPLE AggFuncs (mean & median)
ct_multi = pd.crosstab(
    index=df["Region"],
    columns=df["Product"],
    values=df["Quantity"],
    aggfunc=[np.mean, np.median]
)
print("\nCrosstab: Multiple Aggregations (Mean & Median of Quantity)")
print(ct_multi)
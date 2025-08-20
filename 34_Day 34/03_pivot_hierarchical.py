import pandas as pd

# Sample dataset
data = {
    "Region": ["North", "North", "North", "South", "South", "South", "East", "East"],
    "Department": ["Sales", "Sales", "HR", "Sales", "HR", "IT", "HR", "IT"],
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Salary": [50000, 52000, 48000, 55000, 51000, 60000, 49500, 58000],
    "Bonus": [5000, 5200, 4800, 5500, 5100, 6000, 4950, 5800],
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Pivot table with hierarchical indexing (multi-level rows and columns)
pivot_table = pd.pivot_table(
    df,
    values=["Salary", "Bonus"],
    index=["Region", "Department"],   # Multi-level rows
    columns="Employee",               # Employee as columns
    aggfunc="mean"
)

print("\nHierarchical Pivot Table (Salary & Bonus by Region & Department):")
print(pivot_table)

# Another example: hierarchical rows and multiple aggregation functions
pivot_multi_agg = pd.pivot_table(
    df,
    values="Salary",
    index=["Region", "Department"],   # Multi-level rows
    columns="Employee",
    aggfunc=["mean", "sum"]           # Multiple aggregation functions
)

print("\nHierarchical Pivot Table (Mean & Sum of Salary):")
print(pivot_multi_agg)
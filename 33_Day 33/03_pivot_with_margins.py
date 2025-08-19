# 03_pivot_with_margins.py

import pandas as pd

# Sample dataset: employee performance across departments
data = {
    "Department": ["Sales", "Sales", "Sales", "HR", "HR", "IT", "IT", "IT", "IT"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ian"],
    "Score": [85, 90, 88, 76, 80, 92, 95, 89, 84],
    "Bonus": [500, 700, 600, 400, 450, 800, 850, 750, 650]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df, "\n")

# Pivot table with margins (totals)
pivot_table = pd.pivot_table(
    df,
    index="Department",
    values=["Score", "Bonus"],
    aggfunc={"Score": "mean", "Bonus": "sum"},
    margins=True,          # Adds the totals row
    margins_name="Total"   # Label for totals
)

print("Pivot Table with Margins:\n", pivot_table)
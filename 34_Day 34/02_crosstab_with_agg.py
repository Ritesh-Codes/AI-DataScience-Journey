import pandas as pd

# Sample dataset
data = {
    "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT", "Sales", "HR"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Salary": [50000, 48000, 52000, 51000, 60000, 58000, 55000, 49500]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Crosstab with aggregation function (sum of salaries)
crosstab_sum = pd.crosstab(
    df["Department"],
    df["Gender"],
    values=df["Salary"],
    aggfunc="sum"
)

print("\nCrosstab (Totalsalary by Department and Gender):")
print(crosstab_sum)
# 03_groupby_custom_agg.py
import pandas as pd

# Sample dataset: employee performance
data = {
    "Department": ["HR", "HR", "IT", "IT", "Finance", "Finance", "IT", "HR", "Finance", "IT"],
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Salary": [40000, 42000, 60000, 65000, 50000, 52000, 58000, 41000, 53000, 62000],
    "Bonus": [2000, 2500, 4000, 4200, 3000, 3100, 3500, 2100, 3200, 4100]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Group by Department, apply custom aggregations
custom_agg = df.groupby("Department").agg({
    "Salary": [
        ("Total Salary", "sum"),
        ("Average Salary", "mean"),
        ("Max Salary", "max"),
        ("Salary Range", lambda x: x.max() - x.min())
    ],
    "Bonus": [
        ("Average Bonus", "mean"),
        ("Bonus % of Salary", lambda x: round((x.mean() / df["Salary"].mean()) * 100, 2))
    ]
})

print("\nCustom Aggregations by Department:")
print(custom_agg)

# 2. Example: Group by Department, return top earner's salary
top_salary = df.groupby("Department")["Salary"].apply(lambda x: x.nlargest(1).values[0])
print("\nTop Salary by Department:")
print(top_salary)
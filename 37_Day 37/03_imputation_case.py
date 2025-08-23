import pandas as pd
import numpy as np

# Simulated dataset: Employee performance & salary details
data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G"],
    "Department": ["HR", "Finance", "IT", "Finance", "IT", "HR", "Finance"],
    "Age": [25, 30, np.nan, 45, 28, np.nan, 40],
    "Salary": [50000, 60000, 65000, np.nan, 58000, 52000, np.nan],
    "Performance_Score": [3, np.nan, 4, 5, np.nan, 3, 4]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

# 1. Impute Age with department-wise mean
df["Age_imputed"] = df.groupby("Department")["Age"].transform(
    lambda x: x.fillna(x.mean())
)
print("Age imputed with department-wise mean:\n", df, "\n")

# 2. Impute Salary with overall median
df["Salary_imputed"] = df["Salary"].fillna(df["Salary"].median())
print("Salary imputed with overall median:\n", df, "\n")

# 3. Impute Performance Score with forward fill (temporal assumption)
df["Performance_imputed"] = df["Performance_Score"].fillna(method="ffill")
print("Performance Score imputed with forward fill:\n", df, "\n")

# 4. Final dataset after dropping any remaining missing values
df_final = df.dropna()
print("Final dataset after imputation + dropping remaining nulls:\n", df_final)
import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 30, 45, np.nan],
    "City": ["New York", "Los Angeles", np.nan, "Chicago", "Houston"], 
    "Salary": [50000, 60000, np.nan, 80000, 75000]
}

df = pd.DataFrame(data)
print("Original dataFrame:\n", df, "\n")

# 1. Fill missing Age with mean
df["Age_filled"] = df["Age"].fillna(df["Age"].mean())
print("Fil Age with mean:\n", df, "\n")

# 2. Fill missing Salary with median
df["Salary_filled"] = df["Salary"].fillna(df["Salary"].median())
print("Fill Salary with median:\n", df, "\n")

# 3. Fill missing City with forward fill (previous value)
df["City_filled_ffill"] = df["City"].fillna(method="ffill")
print("Fill City with forward fill:\n", df, "\n")

# 4. Fill missing City with backward fill (next value)
df["City_filled_bfill"] = df["City"].fillna(method="bfill")
print("Fill City with backward fill:\n", df, "\n")

# 5. Fill all missing values with a constant
df_constant = df.fillna("Unknown")
print("Fill all missing values with constant:\n", df_constant, "\n")
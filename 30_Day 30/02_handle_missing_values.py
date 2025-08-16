import pandas as pd

# Sample dataset with missing values
data = {
    "Name": ["Ritesh", "Aman", "Sneha", None, "Priya"],
    "Age": [25, None, 30, 22, None],
    "City": ["Mumbai", "Delhi", None, "Pune", "Chennai"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df, "\n")

# 1. Drop rows with missing values
print("Drop rows with missing values:")
print(df.dropna(), "\n")

# 2. Fill missing values with a constant
print("Fill missing values with a constant value:")
print(df.fillna("Unknown"), "\n")

# 3. Fill missing values with forward fill (propagate previous value)
print("Forward fill (ffill):")
print(df.fillna(method="ffill"), "\n")

# 4. Fill missing values with backward fill
print("Backward fill (bfill):")
print(df.fillna(method="bfill"), "\n")

# 5. Fill missing numerical values with mean
print("Fill numerical values with column mean:")
df_mean_filled = df.copy()
df_mean_filled["Age"] = df_mean_filled["Age"].fillna(df_mean_filled["Age"].mean())
print(df_mean_filled)
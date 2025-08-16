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

# Detect missing values
print("Detect missing values with isnull():")
print(df.isnull(), "\n")

# Count missing values per column
print("Count missing values per column:")
print(df.isnull().sum(), "\n")

# Count total missing values in dataset
print("Total missing values in dataset:")
print(df.isnull().sum().sum())
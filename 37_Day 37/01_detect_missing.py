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
print("Original DataFrame:\n", df, "\n")

# 1. Detect missing values
print("Check missing values (True = Missing):\n", df.isnull(), "\n")

# 2. Count total missing values per column
print("Missing values per column:\n", df.isnull().sum(), "\n")

# 3. Count total missing values in dataset
print("Total missing values in dataset:", df.isnull().sum().sum(), "\n")

# 4. Rows with any missing values
print("Rows with missing values:\n", df[df.isnull().any(axis=1)], "\n")
# 5. Columns with any missing value
missing_cols = df.columns[df.isnull().any()].tolist()
print("Columns with missing values:", missing_cols)
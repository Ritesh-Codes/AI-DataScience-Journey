import pandas as pd
import numpy as np

# Create sample data with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", None],
    "Age": [25, None, 30, 22, 28],
    "City": ["New York", "Los Angeles", None, "Chicago", "Houston"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n",df)

# Detect missing values
print("\nMissiing value check:\n", df.isnull())
print("\nCount of missing values per column:\n", df.isnull().sum())

# Drop missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:\n", df_dropped)
    
    # Fill missing values
df_filled = df.fillna({
    "Name": "Unknown",
    "Age": df["Age"].mean(),
    "City": "Unknown City"
})
print("\nDataFrame after filling missing values:\n", df_filled)

# Save to CSV
df_filled.to_csv("01_pandas_missing_data.csv", index=False)
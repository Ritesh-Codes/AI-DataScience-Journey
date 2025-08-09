# 03_pandas_dataframe_operations.py

import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 75000, 90000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Selecting columns
print("\nSelecting 'Name' column:")
print(df["Name"])

# Selecting multiple columns
print("\nSelecting Name and Salary columns:")
print(df[["Name", "Salary"]])

# Filtering rows
print("\nEmployees with Salary greater than 60,000:")
print(df[df["Salary"] > 60000])

# Adding a new column
df["Bonus"] = df["Salary"] * 0.1
print("\nDataFrame after adding Bonus column:")
print(df)

# Updating values
df.loc[df["Name"] == "Alice", "Salary"] = 55000
print("\nDataFrame after updating Alice's Salary:")
print(df)

# Dropping a column
df = df.drop("Bonus", axis=1)
print("\nDataFrame after dropping Bonus column:")
print(df)
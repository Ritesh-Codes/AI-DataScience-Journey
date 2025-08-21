import pandas as pd

# Sample dataset
data = {
    "Department": ["Sales", "HR", "IT", "Sales", "IT", "HR", "Sales", "IT"],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df, "\n")

# Normalized crosstab (overall proportions)
ct_overall = pd.crosstab(df["Department"], df["Gender"], normalize=True)
print("Normalized Crosstab (Overall proportions):")
print(ct_overall, "\n")

# Row-wise normalization (each department adds up to 1)
ct_row = pd.crosstab(df["Department"], df["Gender"], normalize="index")
print("Normalized Crosstab (Row-wise proportions):")
print(ct_row, "\n")

# Column-wise normalization (each gender adds up to 1)
ct_col = pd.crosstab(df["Department"], df["Gender"], normalize="columns")
print("Normalized Crosstab (Column-wise proportions):")
print(ct_col)
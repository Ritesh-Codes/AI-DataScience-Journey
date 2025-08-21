import pandas as pd

# Sample dataset
data = {
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female"],
    "Purchased": ["Yes", "No", "Yes", "No", "Yes", "Yes", "No", "No"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df, "\n")

# Create a simple crosstab
ct = pd.crosstab(df["Gender"], df["Purchased"])
print("Crosstab of Gender vs Purchased:")
print(ct)
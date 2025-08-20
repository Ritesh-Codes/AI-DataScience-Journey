import pandas as pd

# Sample dataset
data = {
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Purchased": ["Yes", "No", "Yes", "Yes", "No", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Create a crosstab to show frequency of purchases by gender
crosstab = pd.crosstab (df["Gender"], df["Purchased"])

print("\nCrosstab (Purchase Frequency by Gender):")
print(crosstab)
import pandas as pd

# Sample dataset
data = {
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female"],
    "Purchased": ["Yes", "No", "Yes", "No", "Yes", "Yes", "No", "No"],
    "PaymentMethod": ["Card", "Cash", "Card", "UPI", "Cash", "UPI", "Cash", "Card"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df, "\n")

# Crosstab with multiple variables on rows and columns
ct = pd.crosstab(
    index=[df["Gender"], df["Purchased"]], 
# Multi-Index on rows
    columns=df["PaymentMethod"]
# Categories in columns      
)

print("Crosstab with Gender + Purchased vs PaymentMethod:")
print(ct)
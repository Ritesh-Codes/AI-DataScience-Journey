import pandas as pd

# Sample dataset
data = {
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female"],
    "Department": ["IT", "HR", "Finance", "Finance", "IT", "HR", "Finance", "IT"],
    "Status": ["Employed", "Unemployed", "Employed", "Employed", "Unemployed", "Employed", "Unemployed", "Employed"]
}

df = pd.DataFrame(data)
print("Dataset:\n", df, "\n")

# Crosstab with margins (totals)
crosstab_with_margins = pd.crosstab(df["Gender"], df["Status"], margins=True)
print("Crosstab with Margins (Row & Column Totals):\n", crosstab_with_margins, "\n")

# Crosstab with margins and normalized (row-wise)
crosstab_normalized = pd.crosstab(df["Gender"], df["Status"], margins=True, normalize="index")
print("Crosstab with Margins & Normalized (Row-wise Proportions): \n", crosstab_normalized, "\n")

# Crosstab with margins and multi-variable
crosstab_multi_margins = pd.crosstab([df["Gender"], df["Department"]], df["Status"], margins=True)
print("Multi-variable Crosstab with Margins:\n", crosstab_multi_margins)
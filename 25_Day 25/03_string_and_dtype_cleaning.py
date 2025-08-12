# 03_string_and_dtype_cleaning.py
import pandas as pd
import numpy as np

# 1) Create messy DataFrame
data = {
    "Name": [" alice ", "BOB", "ChArLiE  ", "  dave", "Eve#"],
    "Age": ["25", " 30 ", "thirty-five", "-40", "28"],
    "Salary": ["$1000", "$2,000", "3000 USD", "NaN", "4000$"],
    "Join_Date": ["2023-01-15", "15/02/2023", "March 5, 2023", "2023/04/10", "Not Available"]
}

df = pd.DataFrame(data)
print("Original messy DataFrame:\n", df, "\n")

# 2) Clean Name column
df["Name"] = df["Name"].str.strip()         # remove spaces
df["Name"] = df["Name"].str.replace(r"[^a-zA-Z\s]", "", regex=True)  # remove special chars
df["Name"] = df["Name"].str.title()         # proper title case

# 3) Clean Age column
df["Age"] = pd.to_numeric(df["Age"].str.strip(), errors="coerce")  # convert to numeric, invalid -> NaN
df.loc[df["Age"] < 0, "Age"] = np.nan  # remove negative ages

# 4) Clean Salary column
df["Salary"] = df["Salary"].str.replace(r"[^0-9.]", "", regex=True)  # remove $ , letters
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# 5) Clean Join_Date column
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce", dayfirst=True)

# 6) Display cleaned DataFrame
print("Cleaned DataFrame:\n", df, "\n")

# 7) Save cleaned CSV
output_file = "03_string_and_dtype_cleaning_cleaned.csv"
df.to_csv(output_file, index=False)
print(f"Saved cleaned DataFrame to '{output_file}'")
import pandas as pd

# 1. Load dataset
df = pd.read_csv("people_data.csv")
print("Original DataFrame:\n", df)

# -------------------------------
# 2. Convert numeric column stored as string into numeric type
# Let's pretend 'Salary' is read as string
df["Salary"] = df["Salary"].astype(str)  # simulate wrong data type
print("\nSalary column data type before:", df["Salary"].dtype)

# Convert Salary to numeric
df["Salary"] = pd.to_numeric(df["Salary"], errors='coerce')
print("Salary column data type after:", df["Salary"].dtype)

# -------------------------------
# 3. Convert a column to datetime type
# Create a fake 'Joining Date' column for demo
df["Joining Date"] = ["2021-05-10", "2020-07-15", "2022-03-20", "2023-01-05", "2019-09-18",
                      "2021-11-25", "2021-05-10", "2020-12-30", "2022-07-01", "2023-02-14"]

print("\nJoining Date type before:", df["Joining Date"].dtype)
df["Joining Date"] = pd.to_datetime(df["Joining Date"], format="%Y-%m-%d")
print("Joining Date type after:", df["Joining Date"].dtype)

# -------------------------------
# 4. Lowercase all string values in a column
print("\nCity column before lowercasing:\n", df["City"])
df["City"] = df["City"].str.lower()
print("City column after lowercasing:\n", df["City"])

# -------------------------------
# 5. Remove extra spaces from column values
# Add extra spaces for demo
df.loc[0, "Name"] = "  Alice  "
print("\nName before strip:", repr(df.loc[0, "Name"]))
df["Name"] = df["Name"].str.strip()
print("Name after strip:", repr(df.loc[0, "Name"]))

# -------------------------------
# Save cleaned dataset
df.to_csv("people_data_cleaned_v2.csv", index=False)
print("\nCleaned data saved as people_data_cleaned_v2.csv")
# 02_duplicates_handling.py
import pandas as pd

# 1) Create a sample DataFrame with duplicates
data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "David", "Alice"],
    "Age": [25, 30, 25, 35, 30, 40, 25],
    "City": ["NY", "LA", "NY", "Chicago", "LA", "NY", "NY"]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

# 2) Find duplicate rows
duplicates = df.duplicated()
print("Duplicate rows (True means duplicate):\n", duplicates, "\n")

# 3) Remove all duplicates, keep only the first occurrence
df_no_duplicates = df.drop_duplicates()
print("DataFrame without duplicates:\n", df_no_duplicates, "\n")

# 4) Keep only the last occurrence instead
df_keep_last = df.drop_duplicates(keep="last")
print("DataFrame keeping last occurrence:\n", df_keep_last, "\n")

# 5) Remove duplicates based only on 'Name'
df_name_unique = df.drop_duplicates(subset=["Name"])
print("DataFrame with unique names:\n", df_name_unique, "\n")

# 6) Save cleaned version
output_file = "02_duplicates_handling_cleaned.csv"
df_no_duplicates.to_csv(output_file, index=False)
print(f"Saved cleaned DataFrame to '{output_file}'")
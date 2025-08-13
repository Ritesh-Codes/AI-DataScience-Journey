import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:\n", df, "\n")

# --- Renaming columns ---
# Method 1: Using rename() with a dictionary
df_renamed_cols = df.rename(columns={"Name": "Full Name", "Age": "Age (Years)"})
print("After Renaming Columns (Method 1):\n", df_renamed_cols, "\n")

# Method 2: Assigning a new list to columns attribute
df.columns = ["Full Name", "Age", "City"]
print("After Renaming Columns (Method 2 - overwrite all):\n", df, "\n")

# Resetting DataFrame for index renaming
df = pd.DataFrame(data)

# --- Renaming index ---
# Method 1: Using rename() with a dictionary
df_renamed_index = df.rename(index={0: "Row1", 1: "Row2"})
print("After Renaming Index (Method 1):\n", df_renamed_index, "\n")

# Method 2: Assigning a new list to index attribute
df.index = ["Row1", "Row2", "Row3"]
print("After Renaming Index (Method 2 - overwrite all):\n", df, "\n")
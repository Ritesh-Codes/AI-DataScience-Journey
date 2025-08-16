import pandas as pd

# --------------------------
# 1. Create first DataFrame
data1 = {
    "EmployeeID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "Finance", "IT"]
}

df1 = pd.DataFrame(data1)
print("First DataFrame:\n", df1)

# --------------------------
# 2. Create second DataFrame
data2 = {
    "EmployeeID": [104, 105, 106],
    "Name": ["David", "Eva", "Frank"],
    "Department": ["IT", "Marketing", "Finance"]
}

df2 = pd.DataFrame(data2)
print("\nSecond DataFrame:\n", df2)

# --------------------------
# 3. Concatenate vertically (stack rows)
df_vertical = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated Vertically (rows):\n", df_vertical)

# --------------------------
# 4. Concatenate horizontally (side by side)
df_horizontal = pd.concat([df1, df2], axis=1)
print("\nConcatenated Horizontally (columns):\n", df_horizontal)
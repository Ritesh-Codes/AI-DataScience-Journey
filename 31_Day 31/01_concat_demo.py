import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

df2 = pd.DataFrame({
    "ID": [4, 5, 6],
    "Name": ["David", "Eva", "Frank"]
})

# Concatenate row-wise
row_concat = pd.concat([df1, df2])
print("Row-wise Concatenation:")
print(row_concat)

# Concatenate column-wise
col_concat = pd.concat([df1, df2], axis=1)
print("\nColumn-wise Concatenation:")
print(col_concat)
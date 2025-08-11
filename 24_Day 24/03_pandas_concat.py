import pandas as pd

# Step 1: Create two DataFrames
df1 = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})

df2 = pd.DataFrame({
    'name': ['Charlie', 'David'],
    'age': [35, 40]
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Step 2: Vertical concatenation (stack rows)
vertical_concat = pd.concat([df1, df2])
print("\nVertical Concatenation:\n", vertical_concat)

# Step 3: Horizontal concatenation (add columns)
horizontal_concat = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation:\n", horizontal_concat)

# Step 4: Vertical concatenation with ignore_index=True
vertical_ignore_index = pd.concat([df1, df2], ignore_index=True)
print("\nVertical Concatenation with Ignore Index:\n", vertical_ignore_index)

# Step 5: Concatenate with keys
concat_with_keys = pd.concat([df1, df2], keys=['Group1', 'Group2'])
print("\nConcatenation with Keys:\n", concat_with_keys)
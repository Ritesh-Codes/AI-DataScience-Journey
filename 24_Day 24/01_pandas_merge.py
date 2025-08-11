import pandas as pd

# Step 1: Create two DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4], 
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'age': [24, 30, 29, 40]
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Step 2: Inner merge
inner_merge = pd.merge(df1, df2, on='id', how='inner')
print("\nInner Merge:\n", inner_merge)

# Step 3: Left merge
left_merge = pd.merge(df1, df2, on='id', how='left')
print("\nLeft Merge:\n", left_merge)

# Step 4: Right merge
right_merge = pd.merge(df1, df2, on='id', how='right')
print("\nRight Merge:\n", right_merge)

# Step 5: Outer merge
outer_merge = pd.merge(df1, df2, on='id', how='outer')
print("\nOuter Merge:\n", outer_merge)
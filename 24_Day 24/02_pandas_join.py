import pandas as pd

# Step 1: Create two DataFrames with indexes
df1 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}, index=['A', 'B', 'C'])

df2 = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago'],
    'salary': [70000, 80000, 90000]
}, index=['B', 'C', 'D'])

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Step 2: Default join (left join on index)
default_join = df1.join(df2)
print("\nDefault Join:\n", default_join)

# Step 3: Left join
left_join = df1.join(df2, how='left')
print("\nLeft Join:\n", left_join)

# Step 4: Outer join
outer_join = df1.join(df2, how='outer')
print("\nOuter Join:\n", outer_join)

# Step 5: Inner join
inner_join = df1.join(df2, how='inner')
print("\nInner Join:\n", inner_join)
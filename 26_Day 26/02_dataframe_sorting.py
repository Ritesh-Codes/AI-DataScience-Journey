import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 22],
    'Score': [85, 90, 95, 88, 92]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Sorting by a single column (ascending)
df_sorted_age = df.sort_values(by='Age')
print("\nSorted by Age (ascending):")
print(df_sorted_age)

# Sorting by a single column (descending)
df_sorted_score_desc = df.sort_values(by='Score', ascending=False)
print("\nSorted by Score (descending):")
print(df_sorted_score_desc)

# Sorting by multiple columns
df_sorted_multiple = df.sort_values(by=['Score', 'Age'], ascending=[False, True])
print("\nSorted by Score (descending) and Age (ascending):")
print(df_sorted_multiple)

# Resetting index after sorting
df_sorted_reset = df_sorted_multiple.reset_index(drop=True)
print("\nAfter resetting index:")
print(df_sorted_reset)
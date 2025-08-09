# 02_pandas_dataframe.py

import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Access a single column
print("\nNames:")
print(df['Name'])

# Access multiple columns
print("\nNames and Ages:")
print(df[['Name', 'Age']])

# Access rows using loc (label-based)
print("\nRow with index 1 (loc):")
print(df.loc[1])

# Access rows using iloc (integer index)
print("\nRow with index 2 (iloc):")
print(df.iloc[2])

# Filter rows
print("\nPeople older than 30:")
print(df[df['Age'] > 30])
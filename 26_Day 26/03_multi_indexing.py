import pandas as pd

# Creating a sample MultiIndex DataFrame
arrays = [
    ['Region1', 'Region1', 'Region2', 'Region2', 'Region3', 'Region3'],
    ['ProductA', 'ProductB', 'ProductA', 'ProductB', 'ProductA', 'ProductB']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Region', 'Product'))

data = {
    'Sales': [100, 150, 200, 250, 300, 350],
    'Profit': [20, 30, 50, 60, 70, 90]
}

df = pd.DataFrame(data, index=index)

print("MultiIndex DataFrame:")
print(df)

# Selecting all data for Region1
print("\nData for Region1:")
print(df.loc['Region1'])

# Selecting specific data for Region2 and ProductB
print("\nData for Region2, ProductB:")
print(df.loc[('Region2', 'ProductB')])

# Selecting multiple regions
print("\nData for Region1 and Region3:")
print(df.loc[(['Region1', 'Region3'], slice(None)), :])

# Cross-section selection for ProductA across all regions
print("\nCross-section for ProductA across all regions:")
print(df.xs('ProductA', level='Product'))

# Adding a new column based on Sales and Profit
df['Profit Margin'] = df['Profit'] / df['Sales'] * 100
print("\nDataFrame with Profit Margin column:")
print(df)
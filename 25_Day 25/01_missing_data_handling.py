import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
    'Age': [25, np.nan, 30, 22, None],
    'City': ['New York', 'Los Angeles', None, 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

# 1. Detect missing values
print("Missing values (True indicates NaN):\n", df.isna(), "\n")
print("Count of missing values per column:\n", df.isna().sum(), "\n")

# 2. Dropping missing values
df_drop_rows = df.dropna()  # Drop any row with NaN
print("After dropping rows with NaN:\n", df_drop_rows, "\n")

df_drop_cols = df.dropna(axis=1)  # Drop any column with NaN
print("After dropping columns with NaN:\n", df_drop_cols, "\n")

# 3. Filling missing values
df_fill_const = df.fillna("Unknown")  # Fill with a constant value
print("Fill NaN with 'Unknown':\n", df_fill_const, "\n")

df_fill_forward = df.fillna(method='ffill')  # Forward fill
print("Forward fill:\n", df_fill_forward, "\n")

df_fill_backward = df.fillna(method='bfill')  # Backward fill
print("Backward fill:\n", df_fill_backward, "\n")

# 4. Filling numeric columns with mean/median
df_mean_fill = df.copy()
df_mean_fill['Age'] = df_mean_fill['Age'].fillna(df_mean_fill['Age'].mean())
print("Fill 'Age' NaN with mean:\n", df_mean_fill, "\n")

df_median_fill = df.copy()
df_median_fill['Age'] = df_median_fill['Age'].fillna(df_median_fill['Age'].median())
print("Fill 'Age' NaN with median:\n", df_median_fill, "\n")

# 5. Conditional filling
df_conditional = df.copy()
df_conditional['City'] = df_conditional['City'].fillna('Unknown City')
print("Fill 'City' NaN with 'Unknown City':\n", df_conditional, "\n")
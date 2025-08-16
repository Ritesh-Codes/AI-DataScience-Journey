import pandas as pd
import numpy as np

# Create a sample dataset with missing values
data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Temperature": [30, np.nan, 28, np.nan, 27, np.nan, 26]
}

df = pd.DataFrame(data)

print("Original DataFrame with missing values:")
print(df, "\n")

# 1. Linear interpolation
print("Linear Interpolation:")
print(df.interpolate(method="linear"), "\n")

# 2. Quadratic interpolation
print("Quadratic Interpolation:")
print(df.interpolate(method="quadratic"), "\n")

# 3. Polynomial interpolation (order 2)
print("Polynomial Interpolation (order 2):")
print(df.interpolate(method="polynomial", order=2), "\n")

# 4. Time-based interpolation (if index is datetime)
print("Time-based Interpolation:")
df_time = df.copy()
df_time["Date"] = pd.date_range(start="2025-01-01", periods=len(df_time), freq="D")
df_time.set_index("Date", inplace=True)
print(df_time.interpolate(method="time"))
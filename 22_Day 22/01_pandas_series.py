# 01_pandas_series.py
# Day 22 - Assignment 1: Pandas Series Basics

import pandas as pd
import numpy as np

# 1. Create a Series from a Python list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("Series from list:")
print(series_from_list, "\n")

# 2. Create a Series from a NumPy array
data_array = np.array([100, 200, 300, 400, 500])
series_from_array = pd.Series(data_array)
print("Series from NumPy array:")
print(series_from_array, "\n")

# 3. Create a Series from a dictionary
data_dict = {"a": 1, "b": 2, "c": 3}
series_from_dict = pd.Series(data_dict)
print("Series from dictionary:")
print(series_from_dict, "\n")

# 4. Accessing elements by index position
print("Element at index 2 (list series):", series_from_list[2])

# 5. Accessing elements by label (dictionary series)
print("Element with label 'b' (dict series):", series_from_dict["b"], "\n")

# 6. Performing basic operations
print("Addition:", series_from_list + 5)
print("Subtraction:", series_from_list - 5)
print("Mean:", series_from_list.mean())
print("Maximum:", series_from_list.max())
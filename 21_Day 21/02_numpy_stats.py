import numpy as np

# Sample data
data = np.array([12, 15, 20, 21, 21, 22, 24, 30])

# Mean & Median
mean_val = np.mean(data)
median_val = np.median(data)

# Standard Deviation & Variance
std_dev = np.std(data)
variance = np.var(data)

# Min, Max, Range
min_val = np.min(data)
max_val = np.max(data)
range_val = max_val - min_val

# 2D Matrix for axis-based operations
matrix = np.array([[1, 2, 3], [4, 5, 6]])
mean_rows = np.mean(matrix, axis=1)
mean_cols = np.mean(matrix, axis=0)

# Output
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Min:", min_val)
print("Max:", max_val)
print("Range:", range_val)
print("Row-wise Mean:", mean_rows)
print("Column-wise Mean:", mean_cols)
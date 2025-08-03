import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])
print("Original Array:", arr)

# Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("Elements from index 1 to 3:", arr[1:4])
print("Every second element:", arr[::2])

# Modifying elements
arr[2] = 35
print("Updated Array after changing index 2:", arr)

arr[1:4] = [25, 45, 55]
print("Updated Aray after slicing modification:", arr)

# 2D Array indexing/slicing
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", matrix)
print("Element at [1,2]:", matrix [1, 2])
print("First row:", matrix[0])
print("First column:", matrix[:, 0])
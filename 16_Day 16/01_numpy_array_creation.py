import numpy as np

# Basic array from list
arr1 = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr1)

# Array using arange
arr2 = np.arange(10)
print("Array using arange:", arr2)

# Array using linspace
arr3 = np.linspace(0, 1, 5)
print("Array using linspace:", arr3)

# Arrays of zeros and ones
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
print("Zeros array:\n", zeros)
print("Ones array:\n", ones)

# Data type and shape
print("Data type of arr1:", arr1.dtype)
print("Shape of arr2:", arr2.shape)
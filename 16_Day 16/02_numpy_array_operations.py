import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

# Element-wise operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# Universal Functions
print("Square root of arr1:", np.sqrt(arr1))
print("Exponential of arr2:", np.exp(arr2))
print("Mean of arr1:", np.mean(arr1))
print("Max of arr2:", np.max(arr2))

# Broadcasting
arr3 = np.array([5])
print("Broadcasted Assition:", arr1 + arr3) 
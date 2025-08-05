import numpy as np

# Createv array from 10 to 50
arr = np.arange(10, 51)
print("Original Array:\n", arr)

# Elements from index 5 to 15
slice_5_15 = arr[5:16]
print("\nElements from Index 5 to 15:\n", slice_5_15)

# Last 5 elements using negative indexing
last_5 = arr[-5:]
print("\nLast 5 Elements:\n", last_5)

# Every 3rd element in array
every_3rd = arr[::3]
print("\nEvery 3rd Element:\n", every_3rd)

# Reverse array using slicing 
reversed_arr = arr[::-1]
print("\nReversed Array:\n", reversed_arr)
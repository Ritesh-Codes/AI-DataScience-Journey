import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5,6], [7, 8]])

print("Array 1:\n", array1)
print("\nArray 2:\n", array2)

# Vertical Stack
v_stacked = np.vstack((array1, array2))
print("\nVertical Stack:\n", v_stacked)

# Horizontal Stack
h_stacked = np.hstack((array1, array2))
print("\nHorizontal Stack:\n", h_stacked)

# Horizontal Split
h_split = np.hsplit(h_stacked, 2)
print("\nHorizontal Split Result:")
for idx, arr in enumerate(h_split):
    print(f"\nsplit {idx+1}:\n", arr)

# Vertical Split
v_split = np.vsplit(v_stacked, 2)
print("\nvertical Split Result:")
for idx, arr in enumerate(v_split):
    print(f"\nSplit {idx+1}:\n", arr)
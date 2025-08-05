import numpy as np

# Original 1D Array
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original 1D Array:\n", array_1d)

# Reshape to 2D (3x4)
array_2d = array_1d.reshape(3, 4)
print("\nReshaped to 2D (3x4):\n", array_2d)

# Reshape to 2D (4x3)
array_2d_alt = array_1d.reshape(4, 3)
print("\nReshaped to 2D (4x3):\n", array_2d_alt)

# Reshape to 3D (2x3x2)
array_3d = array_1d.reshape(2, 3, 2)
print("\nReshaped to 3D (2x3x2):\n", array_3d)

# Reshape using -1 (auto calculate one dimension)
auto_shape = array_1d.reshape(-1, 6)
print("\nReshaped using -1 (Auto-calc):\n", auto_shape)
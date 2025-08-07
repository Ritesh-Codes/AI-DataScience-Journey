import numpy as np

# Step 1: Create the array
arr = np.array([5, 10, 15, 20, 25, 30])

# Step 2: List of indices you want to access
indices = [0, 2, 4]

# Step 3: Apply fancy indexing 
result = arr[indices]

# Step 4: Output
print("Original Array:", arr) 
print("Selected Indices:", indices)
print("Fancy Indexed Result:", result)
import numpy as np

# Step 1: Create the array
arr = np.array([10, 15, 20, 25, 30,35])\

# Step 2: Apply boolean condition
condition = arr > 20

# Step 3: Index using the condition
result = arr[condition]

# Step 4: Output
print("Original Array:", arr)
print("Condition (arr > 20):", condition)
print("Filtered Result:", result)
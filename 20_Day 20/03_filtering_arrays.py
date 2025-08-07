import numpy as np

# Step 1: Create the array
arr = np.array([12, 7, 19, 3, 24, 10])

# Step 2: Define a filtering condition 
condition = arr > 10

# Step 3: Apply the condition to filter elements
filtered_result = arr[condition]

# Step 4: Output
print("Original Array:", arr)
print("Condtion (arr > 10):", condition)
print("Filtered Array:", filtered_result)
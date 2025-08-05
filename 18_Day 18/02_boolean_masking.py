import numpy as np

# Create array from 1 to 20
arr = np.arange(1, 21)
print("Original Array:\n", arr)

# Mask and print only even numbers 
even_numbers = arr[arr % 2 == 0]
print("\nEven Numbers:\n", even_numbers)

# Mask and print numbers greater than 10
greater_than_10 = arr[arr > 10]
print("\nNumbers greater than 10;\n", greater_than_10)

# Combine conditions: Even numberts greater than 10
even_gt_10 = arr[(arr % 2 == 0) & (arr > 10)]
print("\nEven Numbers Greater than 10:\n", even_gt_10)

# Replace all even numbers with -1
arr[arr % 2 == 0] = -1
print("\nArray after replcing even numbers with -1:\n", arr)
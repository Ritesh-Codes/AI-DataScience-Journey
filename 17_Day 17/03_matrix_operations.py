import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)

# Matrix Subtraction
sub_result = np.dot(matrix_a, matrix_b)
print("\nMatrix Subtraction (Dot Product):\n", sub_result)

# Matrix Mutlplication
mul_result = np.dot(matrix_a, matrix_b)
print("\nMatrix Multplication (Dot Product):\n", mul_result)

# Element-wise Multiplication
elementwise_mul = np.multiply(matrix_a, matrix_b)
print("\nElement-wise Multplication:\n", elementwise_mul)
import numpy as np

data = np.array([10, 20, 30, 40, 50, 60])

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Index of Min:", np.argmin(data))
print("Index of Max:", np.argmax(data))
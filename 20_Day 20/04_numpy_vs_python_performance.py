import numpy as np
import time

# Step 1: Define size
SIZE = 1_000_000

# Step 2: Create datasets
python_list1 = list(range(SIZE))
python_list2 = list(range(SIZE))

numpy_array1 = np.arange(SIZE)
numpy_array2 = np.arange(SIZE)

# Step 3: Measure time for Python list addition
start = time.time()
result = [x + y for x, y in zip(python_list1, python_list2)]
end = time.time()
print("Python List time:", end - start, "seconds")

# Step 4: Measure time for Numpy array addition
start = time.time()
result = numpy_array1 + numpy_array2
end = time.time()
print("Numpy Array Time:", end - start, "seconds")
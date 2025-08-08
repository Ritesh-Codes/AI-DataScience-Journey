import numpy as np

# Random Integer
rand_int = np.random.randint(1, 100)
print("Random Integer:", rand_int)

# Array of Random Integers
rand_int_array = np.random.randint(1, 100, size=5)
print("Array ofRandom Integers:", rand_int_array)

# Random Float
rand_float = np.random.rand()
print("Random Float:", rand_float)

# 2D Array of Random Floats
rand_float_array = np.random.rand(3, 2)
print("2D Array of Random Floats:\n", rand_float_array)

# Set Seed
np.random.seed(42)
seeded_array = np.random.randint(1, 50, size=5)
print("Seeded Random Integers:", seeded_array)

# Normal Distribtion
normal_dist = np.random.normal(loc=0, scale=1, size=(2, 3))
print("Normal Distribution:\n", normal_dist)

# Random Choice
names = ['Ravi', 'Simran', 'Aman', 'Priya']
picked = np.random.choice(names, size=2)
print("Randomly Picked Names:", picked)

# Shuffle Array
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("Shuffules Array:", arr)
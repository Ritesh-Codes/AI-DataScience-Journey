# Creating a tuple with mixed data types
my_tuple = (10, "hello", 3.14, True)
print("Original tuple: ", my_tuple)

# Accessing elements using indexing
print("First Element: ", my_tuple[0])
print("Last Element: ", my_tuple[-1])

# Slicing a tuple
print("First 3 Elements: ", my_tuple[:3])
print("Last 3 Elements: ", my_tuple[-3:])
print("Middle Slice (index 2 to 5): ", my_tuple[2:6])

# Looping through a tuple
for item in my_tuple:
    print("Item: ", item)
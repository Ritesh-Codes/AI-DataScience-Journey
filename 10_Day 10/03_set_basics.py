# Set basics
fruits = { "apple", "banana", "apple", "mango"}
print(fruits)

fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union: ", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
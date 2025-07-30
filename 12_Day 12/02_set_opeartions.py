# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Adding a duplicate to see what happens
my_set.add(3)
print("After adding duplicate 3:", my_set)

# Adding a new element
my_set.add(6)
print("After adding 6:", my_set)

# Two sample sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: all unique elements from both sets
union_set = set_a.union(set_b)
print("Union: ", union_set)

# Interaction: common elements in  both sets
interaction_set = set_a.intersection(set_b)
print("Interaction: ", interaction_set)

# Difference: elements in set_a not in set_b
difference_ab = set_a.difference(set_b)
print("Difference A - B: ", difference_ab)

# Difference: elements in set_b not in set_a
difference_ba = set_b.difference(set_a)
print("Difference B - A: ", difference_ba)

# Symmetric Difference: elements in either set, but not both
sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric Diferenc: ",sym_diff)
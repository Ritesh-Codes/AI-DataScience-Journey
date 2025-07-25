# Multiplication table from 1 to 5
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-" * 15)

# Pattern: Right-angled triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# Outer loop controls rows
# Inner loop controls columns or repeated actions within each row        
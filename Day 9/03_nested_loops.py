for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-----")


for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()        


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
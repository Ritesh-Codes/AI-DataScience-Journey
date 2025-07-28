squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)


squares = [i ** 2 for i in range(10)]
print(squares)


evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)


words = ["python", "is", "fun"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)


matrix = [[col for col in range(3)] for row in range(3)]
print(matrix)
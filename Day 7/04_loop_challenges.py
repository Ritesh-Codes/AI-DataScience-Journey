# Challenge 1: Sum of even numbers from 1 to 100
total = 0
for num in range(1, 101):
    if num % 2 == 0:
        total += num

print("Sum of even numbers from 1 to 100 is: ", total)

# Challenge 2: Find the factorial of a number (e.g., 5)
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} is: ", factorial)

# Challenge 3: Count vowels in a given string
text = "Data Science is fun"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels in'{text}' is: ", count)        
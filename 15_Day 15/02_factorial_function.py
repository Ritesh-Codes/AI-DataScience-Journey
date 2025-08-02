def calculate_factorial():
    n = int(input("Enter a number to calculate factorial: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")

calculate_factorial()
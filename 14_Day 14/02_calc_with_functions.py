def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a ,b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

num1 = float(input("Enter the frist number: "))
operator = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter bthe second number: "))

if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)   
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else: 
    result = "Invalid operator"  
print("Result: ", result)                                         
num1 = float(input("Enter first number: "))
num2= float(input("Enter second number: "))
operation = input("Choose operation (+,-,*,/): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2 
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else: 
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operation."

print("Result", result)            
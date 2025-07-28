# Function with default parameter
def greet(name="Stranger"):
    print(f"Hello, {name}!")

# Function with multiple parameters
def multiply(a, b=1):
    return a * b

# Functions calls using different types of arguments
greet() # Uses default value
greet ("Ritesh") # Uses provided argument 


print("Multiply 3 and 4: ", multiply(3, 4))   # Positional argument
print("Multiply with default b: ", multiply(5))   # b uses default value
print("Using keyword arguments: ", multiply(b=10, a=2))   # Keyword arguments

# greet() will print "Hello, Stranger" if no argument is passed
# multiply() will multiply a and b, b defaults to 1
# You can override defaults or use keywords to change argument order
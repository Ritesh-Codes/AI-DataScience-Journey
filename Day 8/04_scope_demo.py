# Global variable
x = 10

def outer_functions():
    # Enclosing variable
    y = 20

    def inner_functions():
        # Local variable
        z = 30
        print("Inside inner_functions: ")
        print("x (global): ", x)
        print("y (enclosing): ", y)
        print("z (local): ", z)
    inner_functions()

    # Trying to acces z here will fail
    # Print(z)  # Uncomment to see error

outer_functions()

# Accessing x here is fine
print("Outside functions, x: ", x)

# Changing global variable inside a function
def change_global():
    global x
    x = 100
    print("Changed global x inside function: ", x)

change_global()
print("Global x after change: ", x)


# LEGB Rule: Local → Enclosing → Global → Built-in
# Use 'global' to modify global variables inside a function
# Useful for debugging variable shadowing issues
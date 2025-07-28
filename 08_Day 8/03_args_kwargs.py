# Using *args: accepts any number of positional arguments
def add_all(*args):
    print("Received: ", args)
    return sum(args)

print("Sum of all: ", add_all(1, 2, 3, 4, 5))  # Output 15

# Using **kwargs: accepts any number of keyword arguments
def print_user_details(**kwargs):
    print("User details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_details(name="Ritesh", age=25, location="India")

# Mixing *args and **kwargs
def show_data(*args, **kwargs):
    print("Args: ", args)
    print("kwargs: ", kwargs)

show_data(1, 2, 3, name="Ritesh", role="Data Scientist")

# *args collects all extra positional arguments as a tuple
# **kwargs collects all extra keyword arguments as a dictionary
# Useful when you don't know how many arguments will be passed
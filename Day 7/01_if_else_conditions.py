age = int(input("Enter you age: "))

if age < 13:
    print("You're a child.")
elif age >= 13 and age < 20:
    print("You're a teenager.")
elif 20 <= age < 60:
    print("You're an adult.") 
else:
    print("You're a senior citizen.") 

has_license = input("Do you have a driving license? (yes/no): ").lower() == 'yes'
has_vehicle = input("Do you own a vehicle? (yes/no): ").lower() == 'yes'

if has_license and has_vehicle:
    print("You're good to drive!")
elif has_license and not has_vehicle:
    print("You can drive but need to buy/rent a vehicle.")
else:
    print("Sorry, you can't drive.")


# Example of if-elif-else and comparison operators
# Input age and classify based on range

# Example of logical operators (and, or, not)
# Simulating a real-life decision sytem
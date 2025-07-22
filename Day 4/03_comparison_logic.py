 # Assignment 3: Logic with comparisons

is_student = True
is_employed = False

print(is_student and is_employed)     #False
print(is_student or is_employed)      #True
print(not is_student)                 #False

age = int(input("Enter your age: "))
has_license = input("Do you have a license? (yes/no): ").lower() == 'yes'

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")
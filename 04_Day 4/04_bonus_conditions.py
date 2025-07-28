# Assignment 4: Bonus challenge using conditionals

knows_python = input("Do you know Python? (yes/no): ").lower() == 'yes'
has_laptop = input("Do you have a laptop? (yes/no): ").lower() == 'yes'

if knows_python and has_laptop:
    print("You're ready to code!")
else:
    print("You need both skills and tools.")
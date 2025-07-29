name = "Ritesh" 
age = 25
interest = "Data science"

formatted_1 = "My name is {}. I'm {} years old and I love {}.".format(name, age, interest)
print(formatted_1)

formatted_2 = f"My name is {name}. I'm {age} years old and I love {interest}."
print(formatted_2)

print(f"{'Name':<10} | {'Age':^5} | {'Interest':>15}")
print(f"{name:<10} | {age:^5} | {interest:>15}")

height = 5.81234
print(f"My height is {height:.2f} feet.")
name = "Ritesh"
age = 26
learning = True
print(f"My name is {name}, I am {age} years old and learning Python: {learning}")

materials = ["Cement", "Bricks", "Sand","Steel", "Gravel"]
for material in materials:
    print(material)

for i, material in enumerate(materials):
    print(f"{i+1}. {material}")

tools = ["Excavator", "Bulldozer", "Concrete Mixer", "Crane", "Surveying Equipment"] 
for i, tool in enumerate(tools):
    print(f"{i+1}. {tool}")   
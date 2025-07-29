my_string = "  Data Science with Python!  "
print("Original string: ", repr(my_string))

# Remove leading/trailing spaces
stripped = my_string.strip()
print("Stripped:", repr(stripped))

# Convert to lowercase
lower = stripped.lower()
print("Lowercase:", lower)

# Convert to uppercase
upper = stripped.upper()
print("Uppercase:", upper)

# Replace words
replaced = stripped.replace("Python", "AI")
print("Replaced:", replaced)

# Count a character
count_e = stripped.count("e")
print("Count of 'e':", count_e)

# Print first 4 characters
print("First 4 chars:", stripped[:4])

# Last 6 characters
print("Last 6 chars:", stripped[-6:])

# Characters from index 5 to 15
print("Index 5 to 15:", stripped[5:16])

print("'Data' in string?", "Data" in stripped)
print("'Machine' in string?", "Machine" in stripped)
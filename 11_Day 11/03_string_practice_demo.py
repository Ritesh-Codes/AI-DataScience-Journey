text = "Data Science is the future!"

print(text.upper())         # All uppercase
print(text.lower())         # All lowercase
print(text.title())         # Title case
print(text.replace("future", "present"))  # Replace a word
print(text.startswith("Data"))   # Check beginning
print(text.endswith("!"))        # Check end

print(text[0:4])       # First word
print(text[-7:])       # Last word
print(text[::2])       # Every second character

messy = "   Hello, AI world!   "
print(messy.strip())   # Removes whitespace
print(messy.lstrip())  # Removes left space
print(messy.rstrip())  # Removes right space 
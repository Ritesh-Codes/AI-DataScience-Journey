book = {
    "title": "Atomic Habits",
    "author": "James Clear", 
    "pages": 320
}

# Geting keys, values, and items
print(book.keys())  # dict_keys(['title', 'author', 'pages'])
print(book.values())  # dict_values(['Atomic Habits', 'James Clear', 320])
print(book.items())  # dict_items([('title', 'Atomic Habits'), ('author', 'James Clear'), ('pages', 320)])

# Updating the dictionary
book.update({"pages": 350, "published": 2018})
print(book)

# Removing a key
pages = book.pop("pages")
print(f"Removed pages: {pages}")
print(book)

# Clear all (commented out)
# book.clear()
# print(book)
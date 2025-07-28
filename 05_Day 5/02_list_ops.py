# List operation

languages = ["Python", "Java"]
languages.append("C++")
languages.insert(1, "Javascript")

print("After insert: ", languages)

languages.pop()
languages.remove("Java")

print("After pop/remove: ", languages)
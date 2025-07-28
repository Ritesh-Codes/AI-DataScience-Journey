# help() and dir() for debugging

# String
print(help("hello"))
print(dir("hello"))  # Shows available methods

# List
print(help([1, 2, 3]))
print(dir([1, 2, 3]))

# Dictionary
print(help({"x": 5}))
print(dir({"x": 5}))

# BONUS REFLECTION
# If I'm not sure what a string method does, I can use 'help("". replace)' to learn.
# 'type()' is great when you're debugging input issues or checking data types before operations.

# Reflection
# How can type() or help() help you fix bugs or understand errors?
# Where would you use these tools in real-life debugging?
for i in range(10):
    if i == 3:
        break
    print(i)


while True:
    user_input = input("Type something (or 'exit' to quit): ")
    if user_input == "exit":
        break
    print("You typed: ", user_input)
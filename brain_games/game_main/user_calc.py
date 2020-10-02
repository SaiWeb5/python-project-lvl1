def welcome_user():
    name = ""
    while name == "":
        print("Welcome! To the brain games!")
        print("What is the result of a expression?")
        print("\n" "May I have your name? ", end="")
        name = input()
        print("Hello,", name + "! \n" "")
    return name

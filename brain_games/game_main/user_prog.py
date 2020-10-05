def welcome_user():
    name = ""
    while name == "":
        print("Welcome! To the brain games!")
        print("What number is missing in the progression?")
        print("\n" "May I have your name? ", end="")
        name = input()
        print("Hello,", name + "! \n" "")
    return name

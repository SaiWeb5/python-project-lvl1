def welcome_user():
    name = ""
    while name == "":
        print("Welcome! To the brain games!")
        print("Answer \"Yes\" if the number is prime, otherwise \"No\".")
        print("\n" "May I have your name? ", end="")
        name = input()
        print("Hello,", name + "! \n" "")
    return name

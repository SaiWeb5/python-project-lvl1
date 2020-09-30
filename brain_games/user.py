def welcome_user():
    name = ""
    while name == "":
        print("Welcome! \n"
            "Answer \"Yes\" if the number is even, otherwise \"No\". \n"
            "\n"
            "May I have your name? ", end="")
        name = input()
        print("Hello,", name + "! \n"
            "")
    return name

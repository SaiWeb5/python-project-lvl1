import prompt


def welcome_user():
    print("Welcome! To the brain games!")
    print("Answer \"Yes\" if the number is prime, otherwise \"No\".")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    return name

import prompt


def user_public():
    print("Welcome! To the brain games!")
    print("Answer \"Yes\" if the number is even, otherwise \"No\".")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    return name


def user_calc():
    print("Welcome! To the brain games!")
    print("What is the result of a expression?")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    return name


def user_prime():
    print("Welcome! To the brain games!")
    print("Answer \"Yes\" if the number is prime, otherwise \"No\".")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    return name


def user_progression():
    print("Welcome! To the brain games!")
    print("What number is missing in the progression?")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    return name

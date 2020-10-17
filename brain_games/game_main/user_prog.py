import prompt


def welcome_user():
    print("Welcome! To the brain games!")
    print("What number is missing in the progression?")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    return name

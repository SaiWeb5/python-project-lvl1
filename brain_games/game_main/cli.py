import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("\n" "May I have your name? ")
    name = prompt.string("May I have you name? ")
    print("Hello,", name + "!")

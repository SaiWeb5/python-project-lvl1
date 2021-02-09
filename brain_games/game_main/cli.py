import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "!")

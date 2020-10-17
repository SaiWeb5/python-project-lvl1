import prompt


def welcome_user():
    print("Answer something")
    name = prompt.string("May I have you name? ")
    print("Hello,", name + "!")

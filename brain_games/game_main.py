import random
from brain_games.user import welcome_user

def game():
    count = 0
    answer = ""
    solution = 0
    name = welcome_user()
    while count != 3:
        solution = random.randint(0, 20)
        count += 1
        print("Question:", solution)
        print("You answer: ", end="")
        answer = input()
        if solution % 2 == 0 and answer == "Yes":
            print("Correct!")
        elif solution % 2 != 0 and answer == "No":
            print("Ok, true!")
        else:
            print("You are wrong. Correct answer was \"No\". \n"
                "Let's try again,", name + "!")
            break
        if count == 3:
            print("Congratulations,", name + "!")

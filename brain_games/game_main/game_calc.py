import random
from brain_games.game_main.user_calc import welcome_user


def brain_calc():
    count = 0
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y}
    name = welcome_user()
    while count != 3:
        count += 1
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        sum = ('+', '-', '*')
        generate_sum = random.choice(sum)
        solution = operators[generate_sum](num1, num2)
        print('Question:', str(num1), generate_sum, str(num2))
        print('You answer: ', end='')
        answer = input()
        if answer == str(solution):
            print('Correct')
        elif answer != str(solution):
            print(answer, 'is wrong answer. Correct answer was', solution)
            print("Let's try again:", name + "!")
            break
        if count == 3:
            print('Congratulations,', name + "!")

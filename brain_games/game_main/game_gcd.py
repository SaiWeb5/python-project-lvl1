import random
from brain_games.game_main.user_calc import welcome_user


def brain_gcd():
    count = 0
    name = welcome_user()
    while count != 3:
        count += 1
        num1 = random.randint(0, 100)  # Генерируем числа
        num2 = random.randint(0, 100)
        print("Question:", + num1, num2)
        while num1 != 0 and num2 != 0:  # Высчитываем общий делитель
            if num1 > num2:
                num1 %= num2
            else:
                num2 %= num1
        gcd = num1 + num2
        print('You answer: ', end='')
        answer = input()
        if int(answer) == gcd:
            print('Correct')
        elif int(answer) != gcd:
            print(answer, 'is wrong answer. Correct answer was', gcd)
            print("Let's try again:", name + "!")
            break
    if count == 3:
        print("Congratulations,", name + "!")

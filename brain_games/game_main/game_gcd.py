import random


def start_brain_gcd():
    game_over = 0
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
    if str(answer) == str(gcd):
        print('Correct')
        return
    else:
        game_over += 1
        print(answer, 'is wrong answer. Correct answer was', gcd)
        return game_over

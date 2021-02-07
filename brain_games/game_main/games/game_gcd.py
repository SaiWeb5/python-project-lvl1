import random


def start_brain_gcd():
    num1 = random.randint(0, 100)  # Генерируем числа
    num2 = random.randint(0, 100)
    task = '{} {}'.format(str(num1), str(num2))
    while num1 != 0 and num2 != 0:  # Высчитываем общий делитель
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    solution = num1 + num2
    return task, str(solution)

import random


def gen_num():
    num1 = random.randint(0, 100)  # Генерируем числа
    num2 = random.randint(0, 100)
    return num1, num2


def game_gcd():
    value_1 = gen_num()[0]
    value_2 = gen_num()[1]
    task = '{} {}'.format(str(value_1), str(value_2))
    while value_1 != 0 and value_2 != 0:  # Высчитываем общий делитель
        if value_1 > value_2:
            value_1 %= value_2
        else:
            value_2 %= value_1
    solution = value_1 + value_2
    return task, str(solution)

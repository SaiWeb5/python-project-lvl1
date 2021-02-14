import random
import re


def gen_num():
    num_1 = random.randint(10, 60)
    num_2 = random.randint(1, 5)
    return num_1, num_2


def game_progression():
    value_1 = gen_num()[0]
    value_2 = gen_num()[1]
    count = 0
    numbers = []
    while count != 10:  # Генерируем последовательность
        count += 1
        value_1 += value_2
        numbers.append(value_1)
    solution = list(map(str, numbers))
    hide_number = solution[random.randint(0, 8)]
    # Убираем лишние символы
    task = re.sub(hide_number, '..', ' '.join(map(str, numbers)))
    return task, hide_number

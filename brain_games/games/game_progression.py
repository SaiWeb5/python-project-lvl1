import random
import re


def progression_rules():
    return 'What number is missing in the progression?'


def generate_numbers():
    num_1 = random.randint(10, 60)
    num_2 = random.randint(1, 5)
    numbers = []
    for i in range(10):  # Генерируем последовательность
        num_1 += num_2
        numbers.append(num_1)
    return numbers


def game_progression():
    numbers = generate_numbers()
    solution = list(map(str, numbers))
    hide_number = solution[random.randint(0, 8)]
    # Убираем лишние символы
    task = re.sub(hide_number, '..', ' '.join(map(str, numbers)))
    return task, hide_number

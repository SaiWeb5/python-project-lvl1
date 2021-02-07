import random
import re


def start_brain_progression():
    count = 0
    numbers = []
    a = random.randint(10, 60)
    b = random.randint(1, 5)
    while count != 10:  # Генерируем последовательность
        count += 1
        a += b
        numbers.append(a)
    solution = list(map(str, numbers))
    hide_number = solution[random.randint(0, 8)]
    task = re.sub(hide_number, '..', ' '.join(map(str, numbers)))  # Убираем лишние символы
    return task, hide_number

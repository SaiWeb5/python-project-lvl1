import random
import re
PROG_RULES = 'What number is missing in the progression?'


def gen_num():
    num1 = random.randint(10, 60)
    num2 = random.randint(1, 5)
    return num1, num2


def generate_numbers():
    num1, num2 = gen_num()
    numbers = []
    for i in range(10):
        num1 += num2
        numbers.append(num1)
    return numbers


def game_progression():
    numbers = generate_numbers()
    solution = list(map(str, numbers))
    hide_number = solution[random.randint(0, 8)]
    task = re.sub(hide_number, '..', ' '.join(map(str, numbers)))
    return task, hide_number

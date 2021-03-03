import random
PROG_RULES = 'What number is missing in the progression?'


def generate_numbers(num1, num2):
    numbers = []
    for _ in range(10):
        num1 += num2
        numbers.append(num1)
    return numbers


def game_progression():
    num1 = random.randint(10, 60)
    num2 = random.randint(1, 5)
    list_of_numbers = generate_numbers(num1, num2)
    hide_number = list_of_numbers[random.randint(0, 8)]
    replace_number = list(map(lambda x: x if x != hide_number else '..', list_of_numbers))
    task = ' '.join(map(str, replace_number))
    return task, str(hide_number)

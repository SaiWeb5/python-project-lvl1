import random
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
    hide_num = numbers[random.randint(0, 8)]
    replace_num = list(map(lambda x: x if x != hide_num else '..', numbers))
    task = ' '.join(map(str, replace_num))
    return task, str(hide_num)

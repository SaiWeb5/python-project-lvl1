import random
HINT = 'Answer "yes" if the number is even, otherwise "no".'
MIN_NUNBER = 1
MAX_NUMBER = 20


def is_even():
    solution = random.randint(MIN_NUNBER, MAX_NUMBER)
    if solution % 2 == 0:
        return str(solution), 'yes'
    else:
        return str(solution), 'no'

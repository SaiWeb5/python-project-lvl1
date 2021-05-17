import random
HINT = 'Answer "yes" if the number is even, otherwise "no".'
MIN_NUNBER = 1
MAX_NUMBER = 20


def is_even():
    task = random.randint(MIN_NUNBER, MAX_NUMBER)
    if task % 2 == 0:
        return str(task), 'yes'
    else:
        return str(task), 'no'

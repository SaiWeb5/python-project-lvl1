import random
EVEN_RULES = 'Answer "yes" if the number is even, otherwise "no".'


def game_even():
    solution = random.randint(0, 20)
    if solution % 2 == 0:
        return solution, 'yes'
    else:
        return solution, 'no'

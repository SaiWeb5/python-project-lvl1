import random
import operator
HINT = 'What is the result of a expression?'
MIN_NUNBER = 1
MAX_NUMBER = 100


def start_calc():
    num_1 = random.randint(MIN_NUNBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUNBER, MAX_NUMBER)
    operators = ('+', '-', '*')
    random_operator = random.choice(operators)
    task = '{} {} {}'.format(num_1, random_operator, num_2)
    if random_operator == '+':
        solution = operator.add(num_1, num_2)
    elif random_operator == '-':
        solution = operator.sub(num_1, num_2)
    elif random_operator == '*':
        solution = operator.mul(num_1, num_2)
    return task, str(solution)

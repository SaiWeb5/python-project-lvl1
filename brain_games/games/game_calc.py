import random
import operator
CALC_RULES = 'What is the result of a expression?'


def game_calc():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operators = ('+', '-', '*')
    random_operator = random.choice(operators)
    task = '{} {} {}'.format(num1, choose_of_operators, num2)
    if random_operator == '+':
        solution = operator.add(num1, num2)
    elif random_operator == '-':
        solution = operator.sub(num1, num2)
    elif random_operator == '*':
        solution = operator.mul(num1, num2)
    return task, str(solution)

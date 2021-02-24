import random
import operator
CALC_RULES = 'What is the result of a expression?'


def gen_num():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    return num1, num2


def game_calc():
    num1, num2 = gen_num()
    list_of_operators = ('+', '-', '*')
    choose_of_operators = random.choice(list_of_operators)
    if choose_of_operators == '+':
        solution = operator.add(num1, num2)
        task = '{} {} {}'.format(num1, choose_of_operators, num2)
        return task, str(solution)
    if choose_of_operators == '-':
        solution = operator.sub(num1, num2)
        task = '{} {} {}'.format(num1, choose_of_operators, num2)
        return task, str(solution)
    if choose_of_operators == '*':
        solution = operator.mul(num1, num2)
        task = '{} {} {}'.format(num1, choose_of_operators, num2)
        return task, str(solution)

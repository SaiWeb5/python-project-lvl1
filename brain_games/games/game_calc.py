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
    task = '{} {} {}'.format(num1, choose_of_operators, num2)
    if choose_of_operators == '+':
        solution = operator.add(num1, num2)
        return task, str(solution)
    if choose_of_operators == '-':
        solution = operator.sub(num1, num2)
        return task, str(solution)
    if choose_of_operators == '*':
        solution = operator.mul(num1, num2)
        return task, str(solution)
    '''num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operators = {'+': operator.add(num1, num2),
                 '-': operator.sub(num1, num2),
                 '*': operator.mul(num1, num2)}
    print(operators)
    operator_count = ('+', '-', '*')
    select_operator = random.choice(operator_count)
    solution = operators[select_operator]
    task = '{} {} {}'.format(num1, select_operator, num2)
    return task, str(solution)'''

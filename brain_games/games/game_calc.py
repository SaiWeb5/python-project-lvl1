import random
import operator


def calc_rules():
    return 'What is the result of a expression?'


def game_calc():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    # Используем операторы через строку
    operators = {'+': operator.add(num1, num2),
                 '-': operator.sub(num1, num2),
                 '*': operator.mul(num1, num2)}
    operator_count = ('+', '-', '*')
    # Случайный выбор оператора
    select_operator = random.choice(operator_count)
    # Случайная операция над числами
    solution = operators[select_operator]
    task = '{} {} {}'.format(num1, select_operator, num2)
    return task, str(solution)

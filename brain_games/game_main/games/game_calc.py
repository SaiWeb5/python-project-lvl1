import random
import operator


def gen_num():
    num1 = random.randint(0, 100)  # Генерация чисел
    num2 = random.randint(0, 100)
    return num1, num2


def game_calc():
    value_1 = gen_num()[0]
    value_2 = gen_num()[1]
    # Используем операторы через строку
    operators = {'+': operator.add(value_1, value_2),
                 '-': operator.sub(value_1, value_2),
                 '*': operator.mul(value_1, value_2)}
    sum = ('+', '-', '*')
    # Случайный выбор оператора
    generate_sum = random.choice(sum)
    # Случайная операция над числами
    solution = operators[generate_sum]
    task = '{} {} {}'.format(str(value_1), generate_sum, str(value_2))
    return task, str(solution)

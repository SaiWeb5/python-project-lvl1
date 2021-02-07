import random
import operator


def game_calc():
    num1 = random.randint(0, 100)  # Генерация чисел
    num2 = random.randint(0, 100)
    # Используем операторы через строку
    operators = {'+': operator.add(num1, num2),
                 '-': operator.sub(num1, num2),
                 '*': operator.mul(num1, num2)}
    sum = ('+', '-', '*')
    # Случайный выбор оператора
    generate_sum = random.choice(sum)
    # Случайная операция над числами
    solution = operators[generate_sum]
    task = '{} {} {}'.format(str(num1), generate_sum, str(num2))
    return task, str(solution)

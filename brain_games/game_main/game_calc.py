import random


def start_brain_calc():
    # Используем операторы через строку
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y}
    num1 = random.randint(0, 100)  # Генерация чисел
    num2 = random.randint(0, 100)
    sum = ('+', '-', '*')
    # Случайный выбор оператора
    generate_sum = random.choice(sum)
    # Случайная операция над числами
    solution = operators[generate_sum](num1, num2)
    task = str(num1) + ' ' + generate_sum + ' ' + str(num2)
    return task, str(solution)

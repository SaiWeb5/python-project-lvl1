import random


def gen_prime():
    number = random.randint(1, 100)  # Генерируем число
    # Проверяем, является ли число простым
    if number % 2 == 0:
        return number, number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return number, d * d > number


def start_brain_prime():
    task = gen_prime()  # Получаем вопрос и ответ
    # Передаем вопрос и ответ в игровой движок
    if task[1] is True:
        return task[0], 'yes'
    if task[1] is False:
        return task[0], 'no'

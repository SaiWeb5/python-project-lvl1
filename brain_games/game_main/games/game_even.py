import random


def game_even():
    solution = random.randint(0, 20)  # Генерируем число
    # Получаем и отправляем ответ
    if solution % 2 == 0:
        return solution, 'yes'
    if solution % 2 != 0:
        return solution, 'no'

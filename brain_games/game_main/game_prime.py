import random


def gen_num():
    number = random.randint(1, 100)  # Создаем число
    print("Question:", number)
    return number  # И возвращаем его


def gen_prime():
    number = gen_num()  # Получаем число и проверяем, является ли оно простым
    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def start_brain_prime():
    game_over = 0
    result = gen_prime()
    answer = input()
    if result is True and answer == "Yes":  # Проверка ответа игрока
        print("Correct.")
        return
    if result is False and answer == "No":
        print("Correct.")
        return
    if result is True and answer == 'No':
        game_over += 1
        print('Correct answer was: "Yes"')
        return game_over
    if result is False and answer == 'Yes':
        game_over += 1
        print('Correct answer was: "No"')
        return game_over
    else:
        game_over += 1
        print('Incorrect input.')
        return game_over

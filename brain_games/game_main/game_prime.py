import random
from brain_games.game_main.user_prime import welcome_user


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


def game_prime():
    name = welcome_user()  # Приветствие
    result = gen_prime()
    answer = input()
    if result is True and answer == "Yes":  # Проверка ответа игрока
        print("Congratulations,", name + "!")
    elif result is False and answer == "No":
        print("Congratulations,", name + "!")
    else:
        print("You are wrong!" "\n" "Let's try again,", name + "!")

import random


def prime_rules():
    return 'Answer "yes" if the number is prime, otherwise "no".'


def gen_num():
    number = random.randint(1, 100)
    return number


def gen_prime():
    number = gen_num()
    if number % 2 == 0:
        return number, number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return number, d * d > number


def game_prime():
    question, correct_answer = gen_prime()
    # Передаем вопрос и ответ в игровой движок
    if correct_answer is False:
        return question, 'no'
    else:
        return question, 'yes'

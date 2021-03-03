import random
PRIME_RULES = 'Answer "yes" if the number is prime, otherwise "no".'


def find_prime(number):
    if number <= 1:
        return number, False
    if number % 2 == 0:
        return number, number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return number, d * d > number


def game_prime():
    number_test = random.randint(1, 100)
    question, result = find_prime(number_test)
    if result is False:
        return question, 'no'
    else:
        return question, 'yes'

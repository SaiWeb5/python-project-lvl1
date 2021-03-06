import random
HINT = 'Answer "yes" if the number is prime, otherwise "no".'
MIN_NUNBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number <= 1:
        return False
    if number % 2 == 0:
        return number == 2
    odd_divisor = 3
    while odd_divisor * odd_divisor <= number and number % odd_divisor != 0:
        odd_divisor += 2
    return odd_divisor * odd_divisor > number


def start_prime():
    num = random.randint(MIN_NUNBER, MAX_NUMBER)
    result = is_prime(num)
    if not result:
        return num, 'no'
    else:
        return num, 'yes'

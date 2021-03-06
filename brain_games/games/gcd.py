import random
HINT = 'Find the greatest common divisor of given numbers.'
MIN_NUNBER = 1
MAX_NUMBER = 100


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    result = num1 + num2
    return result


def start_gcd():
    num1 = random.randint(MIN_NUNBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUNBER, MAX_NUMBER)
    result = find_gcd(num1, num2)
    task = '{} {}'.format(num1, num2)
    return task, str(result)

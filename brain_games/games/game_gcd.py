import random
GCD_RULES = 'Find the greatest common divisor of given numbers.'


def find_the_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    solution = num1 + num2
    return solution


def game_gcd():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    solution = find_the_gcd(num1, num2)
    task = '{} {}'.format(num1, num2)
    return task, str(solution)

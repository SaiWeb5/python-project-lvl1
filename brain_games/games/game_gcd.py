import random


def gcd_rules():
    return 'Find the greatest common divisor of given numbers.'


def finding_the_divisor():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    while num1 != 0 and num2 != 0:  # Высчитываем общий делитель
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    solution = num1 + num2
    return num1, num2, solution


def game_gcd():
    num1, num2, solution = finding_the_divisor()
    task = '{} {}'.format(num1, num2)
    return task, str(solution)

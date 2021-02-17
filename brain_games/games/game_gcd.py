import random


def gcd_rules():
    return 'Find the greatest common divisor of given numbers.'


def gen_num():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    return num1, num2


def finding_the_divisor():
    num1, num2 = gen_num()
    while num1 != 0 and num2 != 0:  # Высчитываем общий делитель
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    solution = num1 + num2
    return solution


def game_gcd():
    num1, num2 = gen_num()
    solution = finding_the_divisor()
    task = '{} {}'.format(num1, num2)
    return task, str(solution)

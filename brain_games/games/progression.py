import random
HINT = 'What number is missing in the progression?'
MIN_NUNBER = 1
MAX_NUMBER = 60
MIN_NUNBER_STEP = 1
MAX_NUMBER_STEP = 5


def generate_numbers(num1, num2):
    numbers = []
    for _ in range(10):
        num1 += num2
        numbers.append(num1)
    return numbers


def start_progression():
    num1 = random.randint(MIN_NUNBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUNBER_STEP, MAX_NUMBER_STEP)
    progression = generate_numbers(num1, num2)
    hidden_number = progression[random.randint(1, len(progression))]
    replacing_number = [
        number if number != hidden_number else '..'
        for number in progression
    ]
    task = ' '.join(map(str, replacing_number))
    return task, str(hidden_number)

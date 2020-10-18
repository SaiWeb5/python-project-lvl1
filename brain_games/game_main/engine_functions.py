import random
import re
from brain_games.game_main.user import user_public
from brain_games.game_main.user import user_calc
from brain_games.game_main.user import user_progression
from brain_games.game_main.user import user_prime


#  Brain-even
#  ----------
def game_even():
    count = 0
    answer = ""
    solution = 0
    name = user_public()
    while count != 3:
        solution = random.randint(0, 20)  # Генерируем число
        count += 1
        print("Question:", solution)
        print("You answer: ", end="")
        answer = input()
        if solution % 2 == 0 and answer == "Yes":  # Ищем общий делитель
            print("Correct!")
        elif solution % 2 != 0 and answer == "No":
            print("Ok, true!")
        else:
            print("You are wrong.")
            print("Let's try again,", name + "!")
            break
        if count == 3:
            print("Congratulations,", name + "!")


#  Brain-calc
#  ----------
def game_calc():
    count = 0
    # Используем операторы через строку
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y}
    name = user_calc()  # Приветствие игрока
    while count != 3:
        count += 1
        num1 = random.randint(0, 100)  # Генерация чисел
        num2 = random.randint(0, 100)
        sum = ('+', '-', '*')
        generate_sum = random.choice(sum)
        # Случайный выбор оператора
        solution = operators[generate_sum](num1, num2)
        # Случайная операция над числами
        print('Question:', str(num1), generate_sum, str(num2))
        # Проверка ответа, и вывод результатов
        print('You answer: ', end='')
        answer = input()
        if answer == str(solution):
            print('Correct')
        elif answer != str(solution):
            print(answer, 'is wrong answer. Correct answer was', solution)
            print("Let's try again:", name + "!")
            break
        if count == 3:
            print('Congratulations,', name + "!")


#  Brain-gcd
#  ---------
def game_gcd():
    count = 0
    name = user_calc()
    while count != 3:
        count += 1
        num1 = random.randint(0, 100)  # Генерируем числа
        num2 = random.randint(0, 100)
        print("Question:", + num1, num2)
        while num1 != 0 and num2 != 0:  # Высчитываем общий делитель
            if num1 > num2:
                num1 %= num2
            else:
                num2 %= num1
        gcd = num1 + num2
        print('You answer: ', end='')
        answer = input()
        if int(answer) == gcd:
            print('Correct')
        elif int(answer) != gcd:
            print(answer, 'is wrong answer. Correct answer was', gcd)
            print("Let's try again:", name + "!")
            break
    if count == 3:
        print("Congratulations,", name + "!")


#  Brain-progression
#  -----------------
def game_progression():
    count = 0
    a = random.randint(10, 60)
    b = random.randint(1, 10)
    numbers = []
    resultat = ""
    name = user_progression()
    while count != 10:    # Генерируем последовательность
        count += 1
        a += b
        numbers.append(a)
    for i in numbers:           # Создаем строку на вывод пользователю
        resultat = "" .join(str(numbers))
    str_list = list(resultat)
    for i in [13, 14]:    # Скрываем число
        str_list[i] = '.'
    resultat = ''.join(str_list)
    resultat = re.sub(r'[][,]', '', resultat)  # Убираем лишние символы
    print(resultat)
    answer = input()
    if str(numbers[3]) == answer:  # Проверяем ответ
        print("Congratulations,", name + "!")
    else:
        print("No! Correct answer:", numbers[3], "\n" "Try again,", name + "!")


#  Brain-prime
#  -----------
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
    name = user_prime()  # Приветствие
    result = gen_prime()
    answer = input()
    if result is True and answer == "Yes":  # Проверка ответа игрока
        print("Congratulations,", name + "!")
    elif result is False and answer == "No":
        print("Congratulations,", name + "!")
    else:
        print("You are wrong!" "\n" "Let's try again,", name + "!")

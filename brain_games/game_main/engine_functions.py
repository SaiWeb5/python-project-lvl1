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
    game_count = 0
    name = user_progression()
    game_over = 0
    while game_count != 3:
        game_count += 1
        count = 0
        numbers = []
        resultat = ""
        a = random.randint(10, 60)
        b = random.randint(1, 5)
        while count != 10:  # Генерируем последовательность
            count += 1
            a += b
            numbers.append(a)
        for i in numbers:  # Создаем строку на вывод пользователю
            resultat = "".join(str(numbers))
        str_list = list(resultat)
        for i in [13, 14]:  # Скрываем число
            str_list[i] = '.'
        resultat = ''.join(str_list)
        resultat = re.sub(r'[][,]', '', resultat)  # Убираем лишние символы
        print(resultat)
        answer = input()
        if str(numbers[3]) == answer:  # Проверяем ответ
            print("Correct!")
        else:
            game_over += 1
            print("No! Correct answer was:", numbers[3], "\n" "Try again!")
        if game_count == 3:
            print("Congratulations,", name + "!")
        if game_over == 1:
            break


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

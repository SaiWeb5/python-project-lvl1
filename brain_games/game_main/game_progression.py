import random
import re
from brain_games.game_main.user_prog import welcome_user


def brain_progression():
    count = 0
    a = random.randint(10, 60)
    b = random.randint(1, 10)
    numbers = []
    resultat = ""
    name = welcome_user()
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

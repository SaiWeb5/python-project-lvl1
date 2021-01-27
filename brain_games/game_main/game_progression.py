import random
import re


def start_brain_progression():
    game_over = 0
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
        return
    else:
        game_over += 1
        print("No! Correct answer was:", numbers[3])
        return game_over

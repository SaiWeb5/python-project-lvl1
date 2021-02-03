import random
import re


def start_brain_progression():
    count = 0
    numbers = []
    a = random.randint(10, 60)
    b = random.randint(1, 5)
    while count != 10:  # Генерируем последовательность
        count += 1
        a += b
        numbers.append(a)
    resultat = "".join(str(numbers))  # Создаем строку на вывод пользователю
    str_list = list(resultat)
    for i in [13, 14]:  # Скрываем число
        str_list[i] = '.'
    final_string = ''.join(str_list)
    task = re.sub(r'[][,]', '', final_string)  # Убираем лишние символы
    return task, str(numbers[3])

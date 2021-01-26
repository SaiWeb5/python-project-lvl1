import random


def start_brain_even():
    game_over = 0
    solution = random.randint(0, 20)  # Генерируем число
    print("Question:", solution)
    print("You answer: ", end="")
    answer = input()
    if solution % 2 == 0 and answer == "Yes":  # Ищем общий делитель
        print("Correct!")
        return
    if solution % 2 != 0 and answer == "No":
        print("Ok, true!")
        return
    else:
        game_over += 1
        return game_over

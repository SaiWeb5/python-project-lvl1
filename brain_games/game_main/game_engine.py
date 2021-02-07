import prompt


def game_engine(rules, function):
    # Приветствуем игрока и показываем правила игры
    print("Welcome! To the brain games!")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    print(rules())
    for game_level in range(3):
        # Начинаем игру
        # Получаем ответ из игры и задаем вопрос игроку
        answer_from_game = function()
        print('Question:', answer_from_game[0])
        # Ожидаем ответ от игровка
        answer_from_user = prompt.string("You answer: ")
        # Условия победы и поражения
        # Сверяем ответ пользователя с ответом из игры
        if answer_from_game[1] == answer_from_user:
            print('Correct!')
        else:
            print('You are wrong! Correct answer was:', answer_from_game[1])
            print("Let's try again,", name + '!')
            break
        if game_level == 2:
            print("Congratulations,", name + "!")

import prompt


def check_new_system(rules, function):
    # Приветствуем игрока и показываем правила игры
    print("Welcome! To the brain games!")
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    rules()
    round_count = 0
    while round_count != 3:
        # Начинаем игру
        round_count += 1
        # Получаем ответ из игры и задаем вопрос игроку
        answer_from_game = function()
        print('Question:', answer_from_game[0])
        print("You answer: ", end="")
        # Ожидаем ответ от игровка
        answer_from_user = input()
        # Условия победы и поражения
        # Сверяем ответ пользователя с ответом из игры
        if answer_from_game[1] == answer_from_user:
            print('Correct!')
        if answer_from_game[1] != answer_from_user:
            print('You are wrong! Correct answer was:', answer_from_game[1])
            print("Let's try again,", name)
            break
        if round_count == 3:
            print("Congratulations,", name + "!")

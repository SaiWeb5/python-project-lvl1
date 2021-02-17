import prompt


def start_game(rules, game):
    # Приветствуем игрока и показываем правила игры
    round_count = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('\n' 'May I have your name? ')
    print('{}{}{}'.format('Hello, ', name, "! \n"))
    print(rules())
    for game_level in range(round_count):
        # Начинаем игру
        question, correct_answer = game()
        print('Question:', question)
        answer_from_user = prompt.string("You answer: ")
        # Условия победы и поражения
        if correct_answer == answer_from_user:
            print('Correct!')
        else:
            print('You are wrong! Correct answer was:', correct_answer)
            print('{}{}'.format("Let's try again, ", name, '!'))
            break
    else:
        print('{}{}{}'.format('Congratulations, ', name, '!'))

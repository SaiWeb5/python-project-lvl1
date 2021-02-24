import prompt
ROUNDS_COUNT = 3


def start_game(rules, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('\n' 'May I have your name? ')
    print('{}{}{}'.format('Hello, ', name, "! \n"))
    print(rules)
    for _game_level in range(ROUNDS_COUNT):
        question, correct_answer = game()
        print('Question:', question)
        answer_from_user = prompt.string("You answer: ")
        if correct_answer == answer_from_user:
            print('Correct!')
        else:
            print('You are wrong! Correct answer was:', correct_answer)
            print('{}{}{}'.format("Let's try again, ", name, '!'))
            break
    else:
        print('{}{}{}'.format('Congratulations, ', name, '!'))

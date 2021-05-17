import prompt
ROUNDS_COUNT = 3


def start_game(rules, get_task):
    print('Welcome to the Brain Games!')
    name = prompt.string('\n' 'May I have your name? ')
    print('Hello, {}!\n'.format(name))
    print(rules)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_task()
        print('Question: {}!'.format(question))
        answer_from_user = prompt.string("You answer: ")
        if correct_answer == answer_from_user:
            print('Correct!')
        else:
            print('You are wrong! '
                  'Correct answer was: {}!'.format(correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))

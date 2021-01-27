from brain_games.game_main.user import user_public, user_calc, user_gcd, user_progression, user_prime
from brain_games.game_main.game_even import start_brain_even
from brain_games.game_main.game_calc import start_brain_calc
from brain_games.game_main.game_gcd import start_brain_gcd
from brain_games.game_main.game_progression import start_brain_progression
from brain_games.game_main.game_prime import start_brain_prime
import prompt


def check_new_system(rules, function):
    # Приветствуем игрока и показываем правила игры
    print("Welcome! To the brain games!")
    rules()
    name = prompt.string("\n" "May I have your name? ")
    print("Hello,", name + "! \n" "")
    round_count = 0
    # Указываем количество раундов
    while round_count != 3:
        round_count += 1
        error = function()
    # Условия победы и поражения
        if round_count == 3:
            print("Congratulations,", name + "!")
        elif error == 1:
            print("You are wrong.")
            print("Let's try again,", name + "!")
            break

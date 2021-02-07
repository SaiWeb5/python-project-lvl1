from brain_games.game_main.game_engine import check_new_system
from brain_games.game_main.games.game_prime import start_brain_prime
from brain_games.game_main.user import user_prime


def main():
    check_new_system(user_prime, start_brain_prime)


if __name__ == '__main__':
    main()

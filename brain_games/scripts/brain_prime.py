from brain_games.game_main.game_engine import game_engine
from brain_games.game_main.games.game_prime import game_prime
from brain_games.game_main.user import user_prime


def main():
    game_engine(user_prime, game_prime)


if __name__ == '__main__':
    main()

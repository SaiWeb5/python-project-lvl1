from brain_games.game_engine import start_game
from brain_games.games.game_prime import game_prime, PRIME_RULES


def main():
    start_game(PRIME_RULES, game_prime)


if __name__ == '__main__':
    main()

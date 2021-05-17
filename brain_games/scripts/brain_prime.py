from brain_games.game_engine import start_game
from brain_games.games.prime import get_prime, HINT


def main():
    start_game(HINT, get_prime)


if __name__ == '__main__':
    main()

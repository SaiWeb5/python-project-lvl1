from brain_games.game_engine import start_game
from brain_games.games.gcd import get_gcd, HINT


def main():
    start_game(HINT, get_gcd)


if __name__ == '__main__':
    main()

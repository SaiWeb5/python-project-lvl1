from brain_games.game_engine import start_game
from brain_games.games.even import is_even, HINT


def main():
    start_game(HINT, is_even)


if __name__ == '__main__':
    main()

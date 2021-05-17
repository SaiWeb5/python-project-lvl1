from brain_games.game_engine import start_game
from brain_games.games.calc import get_calc, HINT


def main():
    start_game(HINT, get_calc)


if __name__ == '__main__':
    main()

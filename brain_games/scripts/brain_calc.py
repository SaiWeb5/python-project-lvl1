from brain_games.game_engine import start_game
from brain_games.games.calc import start_calc, HINT


def main():
    start_game(HINT, start_calc)


if __name__ == '__main__':
    main()

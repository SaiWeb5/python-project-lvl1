from brain_games.game_engine import start_game
from brain_games.games.game_calc import game_calc, CALC_RULES


def main():
    start_game(CALC_RULES, game_calc)


if __name__ == '__main__':
    main()

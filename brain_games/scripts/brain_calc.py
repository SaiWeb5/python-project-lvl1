from brain_games.game_main.game_engine import game_engine
from brain_games.game_main.games.game_calc import game_calc
from brain_games.game_main.user import user_calc


def main():
    game_engine(user_calc, game_calc)


if __name__ == '__main__':
    main()

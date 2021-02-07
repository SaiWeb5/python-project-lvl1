from brain_games.game_main.game_engine import check_new_system
from brain_games.game_main.games.game_calc import start_brain_calc
from brain_games.game_main.user import user_calc


def main():
    check_new_system(user_calc, start_brain_calc)


if __name__ == '__main__':
    main()

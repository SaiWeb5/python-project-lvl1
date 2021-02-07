from brain_games.game_main.game_engine import check_new_system
from brain_games.game_main.games.game_gcd import start_brain_gcd
from brain_games.game_main.user import user_gcd


def main():
    check_new_system(user_gcd, start_brain_gcd)


if __name__ == '__main__':
    main()

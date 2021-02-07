from brain_games.game_main.game_engine import check_new_system
from brain_games.game_main.games.game_even import start_brain_even
from brain_games.game_main.user import user_public


def main():
    check_new_system(user_public, start_brain_even)


if __name__ == '__main__':
    main()

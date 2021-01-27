from brain_games.game_main.game_engine import check_new_system
from brain_games.game_main.game_progression import start_brain_progression
from brain_games.game_main.user import user_progression



def main():
    check_new_system(user_progression, start_brain_progression)


if __name__ == '__main__':
    main()

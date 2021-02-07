from brain_games.game_main.game_engine import game_engine
from brain_games.game_main.games.game_progression import game_progression
from brain_games.game_main.user import user_progression


def main():
    game_engine(user_progression, game_progression)


if __name__ == '__main__':
    main()

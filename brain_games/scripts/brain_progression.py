from brain_games.game_engine import start_game
from brain_games.games.progression import start_progression, HINT


def main():
    start_game(HINT, start_progression)


if __name__ == '__main__':
    main()

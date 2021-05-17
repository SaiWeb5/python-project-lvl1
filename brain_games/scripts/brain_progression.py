from brain_games.game_engine import start_game
from brain_games.games.progression import get_progression, HINT


def main():
    start_game(HINT, get_progression)


if __name__ == '__main__':
    main()

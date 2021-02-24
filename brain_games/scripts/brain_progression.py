from brain_games.game_engine import start_game
from brain_games.games.game_progression import game_progression, PROG_RULES


def main():
    start_game(PROG_RULES, game_progression)


if __name__ == '__main__':
    main()

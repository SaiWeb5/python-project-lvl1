from brain_games.game_engine import start_game
from brain_games.games.game_progression import game_progression, prog_rules


def main():
    start_game(prog_rules, game_progression)


if __name__ == '__main__':
    main()

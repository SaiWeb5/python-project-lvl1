from brain_games.game_engine import start_game
from brain_games.games.game_progression import game_progression, progression_rules


def main():
    start_game(progression_rules, game_progression)


if __name__ == '__main__':
    main()

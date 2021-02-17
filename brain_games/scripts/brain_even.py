from brain_games.game_engine import start_game
from brain_games.games.game_even import game_even, even_rules


def main():
    start_game(even_rules, game_even)


if __name__ == '__main__':
    main()

from brain_games.game_engine import start_game
from brain_games.games.game_even import game_even, EVEN_RULES


def main():
    start_game(EVEN_RULES, game_even)


if __name__ == '__main__':
    main()

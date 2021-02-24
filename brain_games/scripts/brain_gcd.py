from brain_games.game_engine import start_game
from brain_games.games.game_gcd import game_gcd, GCD_RULES


def main():
    start_game(GCD_RULES, game_gcd)


if __name__ == '__main__':
    main()

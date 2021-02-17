from brain_games.game_engine import start_game
from brain_games.games.game_gcd import game_gcd, gcd_rules


def main():
    start_game(gcd_rules, game_gcd)


if __name__ == '__main__':
    main()

from brain_games.game_main.game_engine import game_engine
from brain_games.game_main.games.game_gcd import game_gcd
from brain_games.game_main.user import user_gcd


def main():
    game_engine(user_gcd, game_gcd)


if __name__ == '__main__':
    main()

from brain_games.game_main.game_engine import game_engine
from brain_games.game_main.games.game_even import game_even
from brain_games.game_main.user import user_public


def main():
    game_engine(user_public, game_even)


if __name__ == '__main__':
    main()

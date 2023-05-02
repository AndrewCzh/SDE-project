"""
This module encapsulates details about games.
"""
import db.db_connect as dbc

COLLECTION = "Games"
DB = "Games"
GAME = 'game'
CNT = 'count'
# TEST_GAME_NAME = 'Test game'
# NUM_PLAYERS = 'num_players'

dbc.connect_db()


def get_games():
    user_ls = dbc.fetch_all(COLLECTION, DB)
    return user_ls


def get_game_details(game):
    filt = {GAME: game}
    info = dbc.fetch_one(COLLECTION, DB, filt)
    if info is not None:
        return info
    else:
        raise ValueError('Game does not exist.')


def count_game():
    return dbc.count(COLLECTION, DB, {})


def main():
    pass
    # game = get_games()
    # print(f'{game=}')
    # print(f'{get_game_details(TEST_GAME_NAME)}')


if __name__ == '__main__':
    main()

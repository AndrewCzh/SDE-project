# from pymongo import MongoClient
import uuid
import db.db_connect as dbc
import server.ingredients_generator as ig

DB = 'Games'
COLLECTION = 'Games'
GAME = 'game'
UID = 'u_id'
sample_uid = "111cdb65-62a8-4df4-b958-550b2921fa86"


def start_game(uid):
    dbc.connect_db()
    game_id = str(uuid.uuid4())
    document = ({UID: uid, GAME: game_id})
    dbc.insert_one(COLLECTION, DB, document)
    data_ls = ig.generator(uid, game_id)
    return data_ls, uid, game_id


def main():
    start_game("111cdb65-62a8-4df4-b958-550b2921fa86")


if __name__ == "__main__":
    main()

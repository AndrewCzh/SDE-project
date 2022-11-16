import os

import pymongo as pm

REMOTE = "0"
LOCAL = "1"

GAME_DB = 'gamedb'

client = None


def connect_db():
    """
    This provides a uniform way to connect to the DB across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    We should probably either return a client OR set a
    client global.
    """
    global client
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("LOCAL_MONGO", LOCAL) == LOCAL:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient("mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients")


def fetch_all(collection, db='Ingredients'):
    ret = []
    for doc in client[db][collection].find():
        del doc['_id']
        ret.append(doc)
    return ret


def fetch_one(collection, db, filt):
    ret = None
    if db == 'Users':
        ret = client[db][collection].find_one(filt)
    # if db == 'Ingredients':
    #     ret = client[db][collection]
    return ret


def fetch_all_as_dict(collection, db, key):
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret


def delete_one(collection, db, filt):
    client[db][collection].delete_one(filt)
    return


def insert_one(collection, db, filt):
    client[db][collection].insert_one(filt)
    return


def main():
    connect_db()
    # print(fetch_all("Burger"))


if __name__ == '__main__':
    main()

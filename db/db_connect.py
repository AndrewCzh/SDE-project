import os

import pymongo as pm

LOCAL = "0"
CLOUD = '1'

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
        print(os.environ.get("CLOUD_MONGO"))
        if os.environ.get("CLOUD_MONGO", LOCAL) == CLOUD:
            password = os.environ.get("GAME_MONGO_PW")
            if not password:
                raise ValueError("You must set your password")
            print("Connecting to Mongo in cloud.")
            client = pm.MongoClient(f"mongodb+srv://jialii:{password}@\
cluster0.wnpabny.mongodb.net/Ingredients")
            # print("CONNECTED")
            # print(password)
        else:
            print("Connect to mongo locally")
            client = pm.MongoClient()


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


def update_one(collection, db, filt, new_values):
    client[db][collection].update_one(filt, new_values)
    return


def main():
    connect_db()
    # print(fetch_all("Burger"))


if __name__ == '__main__':
    main()

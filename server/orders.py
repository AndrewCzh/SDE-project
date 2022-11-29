# from pymongo import MongoClient
import uuid
from bson.json_util import loads

import db.db_connect as dbc
import server.ingredients_generator as ig
import server.check_correct_ingredients as cci

CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


def create_filt(uid, data):
    price_dict = {}
    for d in data:
        # data_ls.append(loads(d))
        price_dict[(loads(d))['name']] = loads(d)['price']
    filt = {"uid": uid, "ing_price": price_dict}
    return filt


def insert_orders(uid, data):

    print("len = ", len(data))
    print("type = ", type(data[0]))
    data_ls = [uid]
    # print("data = ", data)
    # price_dict = {}
    # for d in data:
    #     # data_ls.append(loads(d))
    #     price_dict[(loads(d))['name']] = loads(d)['price']
    filt = create_filt(uid, data)
    price_dict = filt['ing_price']
    data_ls.append(price_dict)
    # insert into orders table
    # client = MongoClient(CONNECTION_STRING)
    # my_db = client["Orders"]
    # my_col = my_db["Orders"]
    # filt = {"uid": uid, "ing_price": price_dict}
    # my_col.insert_one({"uid": uid, "ing_price": price_dict})
    dbc.insert_one("Orders", "Orders", filt)
    return data_ls, filt


def del_orders(uid, data):
    # client = MongoClient(CONNECTION_STRING)
    # my_db = client["Orders"]
    # my_col = my_db["Orders"]
    filt = create_filt(uid, data)
    # filt = {"uid": uid, "ing_price": price_dict}
    dbc.delete_one("Orders", "Orders", filt)


def main():
    dbc.connect_db()
    uid = str(uuid.uuid4())
    data = ig.random_ingredients()
    data_ls = []
    data_price = 0
    for d in data:
        data_ls.append(loads(d)['name'])
        data_price += loads(d)['price']
    order = [uid, data_ls]
    # filt = create_filt(uid, data)
    print(f'{order=},{order[0][0]}')
    insert_orders(uid, data)
    price = cci.check_correct_ingredients(order)
    print(f'{price=}')
    del_orders(uid, data)


if __name__ == "__main__":
    main()

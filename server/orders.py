# from pymongo import MongoClient
import uuid
from bson.json_util import loads
from flask import Flask, jsonify

# import db.db_connect as dbc
from db import db_connect as dbc
import server.ingredients_generator as ig
import server.check_correct_ingredients as cci

CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


def create_filt(uid, game_id, data):
    price_dict = {}
    for d in data:
        # data_ls.append(loads(d))
        price_dict[(loads(d))['name']] = loads(d)['price']
    oid = str(uuid.uuid4())
    filt = {"u_id": uid, 'game': game_id, "oid": oid, "ing_price": price_dict}
    return filt


def insert_orders(uid, game_id, data):
    print("len = ", len(data))
    print("type = ", type(data[0]))
    data_ls = [uid]
    # print("data = ", data)
    # price_dict = {}
    # for d in data:
    #     # data_ls.append(loads(d))
    #     price_dict[(loads(d))['name']] = loads(d)['price']
    filt = create_filt(uid, game_id, data)
    oid = filt['oid']
    price_dict = filt['ing_price']
    data_ls.append(price_dict)
    # insert into orders table
    # client = MongoClient(CONNECTION_STRING)
    # my_db = client["Orders"]
    # my_col = my_db["Orders"]
    # filt = {"uid": uid, "ing_price": price_dict}
    # my_col.insert_one({"uid": uid, "ing_price": price_dict})
    dbc.insert_one("Orders", "Orders", filt)
    return data_ls, oid


def del_orders(oid):
    # client = MongoClient(CONNECTION_STRING)
    # my_db = client["Orders"]
    # my_col = my_db["Orders"]
    filt = ({"oid": oid})
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

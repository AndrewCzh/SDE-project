import pytest
import uuid
from bson.json_util import loads

import server.ingredients_generator as ig
import server.orders as so
import server.check_correct_ingredients as cci
import db.db_connect as dbc

# from pymongo import MongoClient
# list of lists, including uid and ing:price dictionary
orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
             ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
             ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
ret_2 = ["NO FOOD"]

dbc.connect_db()
uid = str(uuid.uuid4())
game_id = str(uuid.uuid4())
data = ig.random_ingredients()
data_ls = []
data_price = 0
for d in data:
    data_ls.append(loads(d)['name'])
    data_price += loads(d)['price']
order = [uid, game_id, data_ls]
# so.insert_orders(uid, data)

# oid = so.insert_orders(uid, game_id, data)[1]


@pytest.fixture(scope='function')
def new_ingredients():
    oid = so.insert_orders(uid, game_id, data)[1]
    print(f"{oid=}")
    yield oid
    so.del_orders(oid)


def test_check_correct_ingredients_correct(new_ingredients):
    oid = new_ingredients
    price = cci.check_correct_ingredients(data_ls, game_id, oid)
    # assert price == data_price
    assert price > 0.0
    assert isinstance(price, float)


def test_check_correct_ingredients_incorrect(new_ingredients):
    oid = new_ingredients
    print(f"{oid=}")
    price = cci.check_correct_ingredients(ret_2, game_id, oid)
    assert price < 0.0
    assert isinstance(price, float)


def main():
    price = cci.check_correct_ingredients(order)
    print(f'{price=}')


if __name__ == "__main__":
    main()

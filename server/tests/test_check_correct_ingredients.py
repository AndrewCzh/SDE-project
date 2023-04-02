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
ret_1 = ["Test User", ["Salad", "Broccoli", "Tuna"]]
ret_2 = ["Test User", ["Salad", "Broccoli"]]

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


@pytest.fixture(scope='function')
def new_ingredients():
    so.insert_orders(uid, game_id, data)
    yield
    so.del_orders(uid, game_id, data)


def test_check_correct_ingredients_correct(new_ingredients):
    price = cci.check_correct_ingredients(order, game_id)
    # assert price == data_price
    assert isinstance(price, float)


def test_check_correct_ingredients_incorrect():
    price = cci.check_correct_ingredients(ret_2, game_id)
    assert price == -1.0
    assert isinstance(price, float)


def main():
    price = cci.check_correct_ingredients(order)
    print(f'{price=}')


if __name__ == "__main__":
    main()

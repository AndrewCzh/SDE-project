import sys
import pytest
from bson.json_util import loads
import server.ingredients_generator as ig
import db.db_connect as dbc
sys.path.append("../../db")
dishi = "Burger"
COLLECTION = 'Burger'


@pytest.fixture(scope='function')
def new_food_type():
    dbc.insert_one(COLLECTION, ig.DB, {{'name': 'Bread', 'price': 7.0},
                                       {'name': 'Bacon', 'price': 1.5},
                                       {'name': 'Cheese', 'price': 1},
                                       {'name': 'Pickles', 'price': 0.5},
                                       {'name': 'Tomato', 'price': 0.5},
                                       {'name': 'Lettuce', 'price': 0.5},
                                       {'name': 'Mushroom', 'price': 0.5},
                                       {'name': 'Grilled Mushroom', 'price': 0.5},
                                       {'name': 'Onions', 'price': 0.5},
                                       {'name': 'Beef', 'price': 3}})
    yield
    dbc.delete_all(COLLECTION, ig.DB)


def test_get_ingredients_price_details():
    price = ig.get_ingredients_price_details()
    assert isinstance(price, list)


def test_dish_generate():
    dish = ig.dish_generate()
    assert isinstance(dish, str)
    assert dish in ig.dishes


def test_random_ingredients():
    ing_ls = ig.random_ingredients()
    assert isinstance(ing_ls, list)
    assert len(ing_ls) >= 1


def test_random_ingredients_not_duplicate():
    ing_ls = ig.random_ingredients()
    print(f'{ing_ls=}')
    visited = dict()
    for ing in ing_ls:
        ing = loads(ing)
        if ing['name'] not in visited:
            visited[ing['name']] = ing
        else:
            assert 0 == 1
    assert len(visited) == len(ing_ls)


def test_match_dish():
    dish = ig.match_dish(dishi)
    assert isinstance(dish, str)

import sys
from bson.json_util import loads

sys.path.append("../../db")
import server.ingredients_generator as ig

dishi = "Burger"


def test_dish_generate():
    dish = ig.dish_generate()
    assert isinstance(dish, str)
    assert dish in ig.dishes


def test_random_ingredients():
    ing_ls = ig.random_ingredients()
    assert isinstance(ing_ls, list)
    assert len(ing_ls) > 1


def test_random_ingredients_not_duplicate():
    ing_ls = ig.random_ingredients()
    visited = dict()
    for ing in ing_ls:
        ing = loads(ing)
        if ing['_id'] not in visited:
            visited[ing['_id']] = ing['_id']
        else:
            assert 0 == 1
    assert len(visited) == len(ing_ls)


def test_match_dish():
    dish = ig.match_dish(dishi)
    assert isinstance(dish, str)

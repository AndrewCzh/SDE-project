import server.check_correct_ingredients as cci

# from pymongo import MongoClient
# list of lists, including uid and ing:price dictionary
orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
             ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
             ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
ret_1 = ["Test User", ["Salad", "Broccoli", "Tuna"]]
ret_2 = ["Test User", ["Salad", "Broccoli"]]


def test_check_correct_ingredients_correct():
    price = cci.check_correct_ingredients(ret_1)
    assert price == 7.5
    assert isinstance(price, float)


def test_check_correct_ingredients_incorrect():
    price = cci.check_correct_ingredients(ret_2)
    assert price == -1.0
    assert isinstance(price, float)

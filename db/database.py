"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
from pymongo import MongoClient
import random

dishes = ["Burger", "Pizza", "PokeBowl", "Salad", "Sushi"]
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


def dataInsert():
    client = MongoClient(CONNECTION_STRING)
    docs = [
        # set bread to $7 since the burger costs $7
        {"name": "Rice", "price": 7.0},
        {"name": "Zucchini", "price": 0.5},
        {"name": "Avocado", "price": 1.0},
        {"name": "Shrimp", "price": 1.0},
        {"name": "Broccoli", "price": 0.5},
        {"name": "Chicken", "price": 1.0},
        {"name": "Salmon", "price": 1.0},
        {"name": "Tuna", "price": 1.0},
        ]

    client.Ingredients.Sushi.insert_many(docs)  # change collection name


def dish_generate():
    """
    Returns a random dish
    """
    index = random.randrange(len(dishes))
    return dishes[index]


def random_ingredients():
    """
    Returns a list of ingredients
    """
    ret = []
    cnt1 = 0
    cnt2 = 0
    dish = dish_generate()
    client = MongoClient(CONNECTION_STRING)
    my_db = client["Ingredients"]
    my_col = my_db[dish]
    ingredients = my_col.find()  # return a cursor

    total_count = my_col.count_documents({})
    ing_num = random.randint(1, total_count-1)
    ls = [i for i in range(1, total_count)]
    ing_ls = random.sample(ls, ing_num)
    ing_ls.sort()

    for ing in ingredients:
        if cnt1 == 0:
            ret.append(ing)
        if cnt2 < len(ing_ls) and cnt1 == ing_ls[cnt2]:
            ret.append(ing)
            cnt2 += 1
        cnt1 += 1

    return ret


def fetch_pets():
    """
    A function to return all pets in the data store.
    """
    return {"tigers": 2, "lions": 3, "zebras": 1}


def main():
    ls = random_ingredients()
    print(ls)


if __name__ == "__main__":
    main()

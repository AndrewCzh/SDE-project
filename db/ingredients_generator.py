from pymongo import MongoClient
from bson.json_util import dumps
import random

dishes = ["Burger", "Pizza", "PokeBowl", "Salad", "Sushi"]
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


def dish_generate():
    """
    Returns a random dish
    """
    index = random.randrange(len(dishes))
    return dishes[index]


def random_ingredients():
    """
    Returns a list of ingredients
    json.dumps is used to convert objectId to $oid
    to convert it back using loads()
    """
    ret = []
    cnt1 = 0
    cnt2 = 0
    dish = dish_generate()
    # print(dish)
    client = MongoClient(CONNECTION_STRING)
    my_db = client["Ingredients"]
    my_col = my_db[dish]
    ingredients = my_col.find()  # return a cursor

    total_count = my_col.count_documents({})
    ing_num = random.randint(1, total_count-1)
    ls = [i for i in range(1, total_count)]
    # print(ls)
    # print(ing_num)
    ing_ls = random.sample(ls, ing_num)
    ing_ls.sort()
    # print(ing_ls)

    for ing in ingredients:
        if cnt1 == 0:
            ret.append(dumps(ing))
        if cnt2 < len(ing_ls) and cnt1 == ing_ls[cnt2]:
            ret.append(dumps(ing))
            cnt2 += 1
        cnt1 += 1

    # ing_ls = list(ingredients)  # possibly not good for a large size of data
    # print("len(ing_ls) = ", len(ing_ls))
    # ing_num = random.randint(0, len(ing_ls)-1)
    # print("ing_num = ", ing_num)
    #
    # ret = random.sample(ing_ls[1:], ing_num)
    # ret.append(ing_ls[0])
    # print("len(ret) = ", len(ret))

    # print('kkkkk')
    # if isinstance(ret[0], str):
    #     print(ret[0])
    #     x = loads(ret[0])
    #     if isinstance(x, dict):
    #         print(x)
    return ret


def main():
    ls = random_ingredients()
    print(ls)


if __name__ == "__main__":
    main()

from pymongo import MongoClient
from bson.json_util import dumps, loads
import random
from flask import Flask

from server import orders as so
# from server import orders as so
# import server.orders as so

app = Flask(__name__)

dishes = ["Burger", "Pizza", "PokeBowl", "Salad", "Sushi"]
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


# @app.route('/', methods=['GET', 'POST'])
def generator(uid, game_id):
    data = random_ingredients()
    # print("len = ", len(data))
    # print("type = ", type(data[0]))
    # data_ls = [uid]
    # # print("data = ", data)
    # price_dict = {}
    # for d in data:
    #     # data_ls.append(loads(d))
    #     price_dict[(loads(d))['name']] = loads(d)['price']
    # data_ls.append(price_dict)
    # # insert into orders table
    # client = MongoClient(CONNECTION_STRING)
    # my_db = client["Orders"]
    # my_col = my_db["Orders"]
    # filt = {"uid": uid, "ing_price": price_dict}
    # so.insert_orders(my_col, my_db, filt)
    # # my_col.insert_one({"uid": uid, "ing_price": price_dict})
    data_ls, oid = so.insert_orders(uid, game_id, data)
    print(f'{data_ls=}')
    print("type = ", type(data_ls[1]))
    # return render_template('home.html', data_ls=data_ls)
    return data_ls, oid

# @app.route('/home')
# def home():
#     return render_template('home.html')


def get_ingredients_price_details():
    data = random_ingredients()
    data_ls = []
    for d in data:
        d = loads(d)
        del d["_id"]
        data_ls.append(d)
    # return data_ls[0].get('price', None)
    return data_ls


def dish_generate():
    """
    Returns a random dish
    """
    index = random.randrange(len(dishes))
    return dishes[index]


def match_dish(dish):
    if dish == "Burger":
        return "Bread&Meat"
    elif dish == "Pizza":
        return "Crust"
    elif dish == "PokeBowl":
        return "RiceBowl"
    elif dish == "Salad":
        return "Salad"
    elif dish == "Sushi":
        return "Rice"
    else:
        return ""


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
    major = my_col.find({"name": match_dish(dish)})
    print(major)

    # print(ing_ls)
    for ing in ingredients:
        if cnt1 == 0:
            ret.append(dumps(major[0]))
        if cnt2 < len(ing_ls) and cnt1 == ing_ls[cnt2]:
            if ing["name"] == match_dish(dish):
                continue
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
    data = random_ingredients()
    # print("len = ", len(data))
    # print("type = ", type(data[0]))
    # data_ls = []
    print("data = ", data)
    # data_ls = []
    # data_price = 0
    # for d in data:
    #     data_ls.append(loads(d)['name'])
    #     data_price += loads(d)['price']
    # order = [data_ls]
    # print(f'{order=},{order[0][0]}')
    # app.run()

    # print("here = ", get_ingredients_price_details())


if __name__ == "__main__":
    main()
    # ingred = random_ingredients()
    # print(f"{ingred=}")
    ret = get_ingredients_price_details()
    # print(f"{ret=}")

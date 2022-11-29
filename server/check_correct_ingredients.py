from pymongo import MongoClient

# list of lists, including uid and ing:price dictionary
orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
             ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
             ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
ret = ["Test User", ["Salad", "Broccoli", "Tuna"]]

# Prepare db connection
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


# check whether there is a order returned by the user in the order_tb
def check_correct_ingredients(order):
    # length = len(orders_tb) - 1
    # u_id = order[0]
    # cnt = 0
    u_id = order[0]
    client = MongoClient(CONNECTION_STRING)
    my_db = client["Orders"]
    my_col = my_db["Orders"]
    found = my_col.find({"uid": u_id})
    # print(found)
    for item in found:
        end = True
        money = 0
        if len(item["ing_price"]) == len(order[1]):
            for food in order[1]:
                if food not in item["ing_price"]:
                    end = False
                    break
                else:
                    money += item["ing_price"][food]
            if end:
                return float(money)
    return -1.0

    # for item in orders_tb:
    #     money = 0
    #     end = True
    #     if item[0] == u_id:
    #         if len(item[1]) == len(order[1]):
    #             for food in order[1]:
    #                 if food not in item[1]:
    #                     end = False
    #                     break
    #                 else:
    #                     money += item[1][food]
    #             if end:
    #                 orders_tb[cnt], orders_tb[length] = \
    #                     orders_tb[length], orders_tb[cnt]
    #                 orders_tb.pop()
    #                 return float(money)
    #     cnt += 1
    # return -1.0


def main():
    order = ["4de4cbcd-5cd3-495c-bb81-b1c60ea93753",
             ["Salad", "Lettuce"]]
    money = check_correct_ingredients(order)
    print(money)


if __name__ == "__main__":
    main()

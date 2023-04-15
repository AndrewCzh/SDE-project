from db import db_connect as dbc


# list of lists, including uid and ing:price dictionary
orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
             ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
             ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
ret = ["Test User", ["Salad", "Broccoli", "Tuna"]]


# check whether there is a order returned by the user in the order_tb
def check_correct_ingredients(order, game, oid):
    dbc.connect_db()
    filt = {"game": game, "oid": oid}
    found = dbc.fetch_one("Orders", "Orders", filt)
    money = 0.0
    print(f"{found=}")

    if found:
        for ing in order:
            if ing in found['ing_price']:
                money += float(found['ing_price'][ing])
            else:
                money -= 0.5
        print(f'inside check_correct_ingredient = {money}')
        return money
    else:
        return -1
    # # print(found)
    # for item in found:
    #     end = True
    #     money = 0
    #     if len(item["ing_price"]) == len(order[2]):
    #         for food in order[2]:
    #             if food not in item["ing_price"]:
    #                 end = False
    #                 break
    #             else:
    #                 money += item["ing_price"][food]
    #         if end:
    #             return float(money)
    # return -1.0


def main():
    # order = ["4de4cbcd-5cd3-495c-bb81-b1c60ea93753",
    #          ["Salad", "Lettuce"]]
    # money = check_correct_ingredients([],
    # "ab038374-8f6a-4d0c-b269-a512dd013cb6", "")
    # print(money)
    print()


if __name__ == "__main__":
    main()

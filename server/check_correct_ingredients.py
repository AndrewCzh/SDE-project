from db import db_connect as dbc


# list of lists, including uid and ing:price dictionary
orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
             ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
             ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
ret = ["Test User", ["Salad", "Broccoli", "Tuna"]]


# check whether there is a order returned by the user in the order_tb
def check_correct_ingredients(order, game):
    dbc.connect_db()
    filt = {"uid": order[0], "game": game}
    found = dbc.fetch_all_with_filt("Orders", "Orders", filt)

    # print(found)
    for item in found:
        end = True
        money = 0
        if len(item["ing_price"]) == len(order[2]):
            for food in order[2]:
                if food not in item["ing_price"]:
                    end = False
                    break
                else:
                    money += item["ing_price"][food]
            if end:
                return float(money)
    return -1.0


def main():
    order = ["4de4cbcd-5cd3-495c-bb81-b1c60ea93753",
             ["Salad", "Lettuce"]]
    money = check_correct_ingredients(order)
    print(money)


if __name__ == "__main__":
    main()

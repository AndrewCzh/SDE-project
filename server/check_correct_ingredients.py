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
                print(f"money = {money}")
            else:
                money -= 0.5
        print(f'inside check_correct_ingredient = {money}')
        return money
    else:
        return -1


def main():
    print()


if __name__ == "__main__":
    main()

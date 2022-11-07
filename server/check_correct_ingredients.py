# list of lists, including uid and ing:price dictionary
orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
             ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
             ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
ret = ["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]


# check whether there is a order returned by the user in the order_tb
def check_correct_ingredients(order):
    length = len(orders_tb) - 1
    uid = order[0]
    cnt = 0
    for item in orders_tb:
        money = 0
        end = True
        if item[0] == uid:
            if len(item[1]) == len(order[1]):
                for food in order[1].keys():
                    if food not in item[1]:
                        end = False
                        break
                    else:
                        money += order[1][food]
                if end:
                    orders_tb[cnt], orders_tb[length] = \
                        orders_tb[length], orders_tb[cnt]
                    orders_tb.pop()
                    return float(money)
        cnt += 1
    return -1.0


def main():
    money = check_correct_ingredients(ret)
    print(money)


if __name__ == "__main__":
    main()

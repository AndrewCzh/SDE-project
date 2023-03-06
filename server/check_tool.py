from pymongo import MongoClient

# list of lists, including uid and ing:price dictionary
# orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
#              ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
#              ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
# ret = ["Test User", ["Salad", "Broccoli", "Tuna"]]

# Prepare db connection
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/cooktool"


def main():
#     order = ["4de4cbcd-5cd3-495c-bb81-b1c60ea93753",
#              ["Salad", "Lettuce"]]
#     money = check_correct_ingredients(order)
#     print(money)


if __name__ == "__main__":
    main()

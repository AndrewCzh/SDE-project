from pymongo import MongoClient
import pymongo

# cook_tools = {'food1': 'A', 'food2': 'B', 'food3': 'C'}

# def can_cook(food, cook_tool):
#     if cook_tools[food] == cook_tool:
#         return True
#     else:
#         return False


# list of lists, including uid and ing:price dictionary
# orders_tb = [["Test User", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}],
#              ["Test User", {"RiceBowl": 7, "Shrimp": 1, "Broccoli": 0.5}],
#              ["Bowen", {"Salad": 6, "Broccoli": 0.5, "Tuna": 1}]]

# User's return from the front-end
# ret = ["Test User", ["Salad", "Broccoli", "Tuna"]]

# Prepare db connection
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/cooktool"


# def main():
#     order = ["4de4cbcd-5cd3-495c-bb81-b1c60ea93753",
#              ["Salad", "Lettuce"]]
#     money = check_correct_ingredients(order)
#     print(money)
# Define MongoDB connection parameters


client = MongoClient('localhost', 27017)
db = client['cooktool']


# Define function to check if a tool exists in a collection
def check_tool(collection_name, tool_name):
    collection = db[collection_name]
    tool = collection.find_one({"name": tool_name})
    if tool is None:
        print("The tool {} does not exist in the collection {}"
              .format(tool_name, collection_name))
    else:
        print("The tool {} exists in the collection {}"
              .format(tool_name, collection_name))


# Test function with a wrong tool name
def test_wrong_tool():
    check_tool("measuring_cups", "potato masher")

# Connect to the database and call the test function


def fetch_cooktool(name):
    # connect to the MongoDB server and select the "cooktools" database
    client = pymongo.MongoClient()
    db = client['cooktools']

    # select the "tools" collection and find the cooktool with the given name
    collection = db['tools']
    tool = collection.find_one({'name': name})

    # return the cooktool as a dictionary
    return tool


def test_fetch_cooktool():
    # fetch the "spoon" cooktool
    spoon = fetch_cooktool('spoon')

    # assert that the fetched cooktool is not None
    assert spoon is not None

    # assert that the fetched cooktool has the correct name
    assert spoon['name'] == 'spoon'

    # assert that the fetched cooktool has the correct description
    assert spoon['description'] == 'A utensil consisting of a \
    small shallow bowl, oval or round, at the end of a handle.'

    # assert that the fetched cooktool has the correct usage
    assert spoon['usage'] == 'Stirring, serving, and mixing \
    ingredients in cooking and baking.'


if __name__ == "__main__":
    test_wrong_tool()

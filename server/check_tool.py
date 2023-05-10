from pymongo import MongoClient
import pymongo

# Prepare db connection
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/cooktool"


client = MongoClient('localhost', 27017)
db = client['cooktool']


def check_correct_tool(data, data2):
    money = 0.0
    if len(data2) == 0 or len(data2) > 1:
        money -= 5
    elif data[0] == 'Bread' and data2[0] == 'Grill':
        money += 5
    elif data[0] == 'Crust' and data2[0] == 'Oven':
        money += 5
    elif data[0] == 'Rice' and data2[0] == 'RiceCooker':
        money += 5
    elif data[0] == 'Salad_Dressing' and data2[0] == 'RiceCooker':
        money += 5
    else:
        money -= 5
    return money


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

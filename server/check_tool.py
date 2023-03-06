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
        print("The tool {} does not exist in the collection {}".format(tool_name, collection_name))
    else:
        print("The tool {} exists in the collection {}".format(tool_name, collection_name))

# Test function with a wrong tool name
def test_wrong_tool():
    check_tool("measuring_cups", "potato masher")

# Connect to the database and call the test function


if __name__ == "__main__":
    test_wrong_tool()

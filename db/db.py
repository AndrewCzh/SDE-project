"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""
import pymongo
from pymongo import MongoClient

def dataInsert():
    CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@cluster0.wnpabny.mongodb.net/Ingredients"
    client = MongoClient(CONNECTION_STRING)
    #db = client.Ingredients
    #coll = db.Sushi
    docs = [
        {"name": "Rice", "price": 7.0}, #set bread to $7 since the burger costs $7
        {"name": "Zucchini", "price": 0.5},
        {"name": "Avocado", "price": 1.0},
        {"name": "Shrimp", "price": 1.0},
        {"name": "Broccoli", "price": 0.5},
        {"name": "Chicken", "price": 1.0},
        {"name": "Salmon", "price": 1.0},
        {"name": "Tuna", "price": 1.0},
        ]

    client.Ingredients.Sushi.insert_many(docs) #change collection name

def fetch_pets():
    """
    A function to return all pets in the data store.
    """
    return {"tigers": 2, "lions": 3, "zebras": 1}

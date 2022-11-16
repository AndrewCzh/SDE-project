"""
This module encapsulates details about users.
"""
from pymongo import MongoClient
# from bson.json_util import dumps
import uuid
import db.db_connect as dbc

TEST_USER_NAME = 'Test user'
TEST_UID = '111cdb65-62a8-4df4-b958-550b2921fa86'
SAMPLE_USER = "Sample User"
NAME = 'name'
UID = 'u_id'
FULL_NAME = 'full_name'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.
REQUIRED_FLDS = [UID, NAME]
users = {TEST_USER_NAME: {UID: '05bfb803-dc3a-4379-ac49-aa9c809fda5b',
                          FULL_NAME: 'Porgy Tirebiter'},
         'handle': {UID: 'kkkk', FULL_NAME: 'Nick Danger'}}
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"
client = MongoClient(CONNECTION_STRING)
my_db = client["Users"]
my_col = my_db["Users"]
COLLECTION = "Users"
DB = "Users"

dbc.connect_db()


def user_exists(uid, name):
    """
    Returns whether or not a user exists.
    """
    # user = my_col.find_one({UID: uid, NAME: name})  # return a cursor
    filt = {UID: uid, NAME: name}
    user = dbc.fetch_one(COLLECTION, DB, filt)
    return user is not None


def get_users_dict():
    users_dict = dbc.fetch_all_as_dict(COLLECTION, DB)
    return users_dict


def get_users():
    # user_ls = my_col.find({})
    # ls = []
    # for user in user_ls:
    #     ls.append(dumps(user))
    users_ls = dbc.fetch_all(COLLECTION, DB)
    return users_ls


def get_user_details(uid):
    # user = my_col.find_one({UID: uid})
    filt = {UID: uid}
    user = dbc.fetch_one(COLLECTION, DB, filt)
    if user is not None:
        return user
    else:
        raise ValueError('User is not exist.')


def del_user(uid):
    filt = {UID: uid}
    # my_col.delete_one({UID: uid})
    dbc.delete_one(COLLECTION, DB, filt)
    return


# def del_all():
#     my_col.delete_many({})
#     return


def add_user(name):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    # if not isinstance(details, dict):
    #     raise TypeError(f'Wrong type for details: {type(details)=}')
    # for field in REQUIRED_FLDS:
    #     if field not in details:
    #         raise ValueError(f'Required {field=} missing from details')
    # max_id = my_col.find().sort("u_id", -1).limit(1)
    uid = 0
    found = 1
    while found:
        uid = str(uuid.uuid4())
        filt = {UID: uid}
        found = dbc.fetch_one(COLLECTION, DB, filt)
    document = ({UID: uid, NAME: name})
    # users[name] = details
    dbc.insert_one(COLLECTION, DB, document)
    return uid


def main():
    # del_all()
    print("here")
    # temp = user_exists("Sample User")
    # print(f"{temp=}")
    # user_ls = get_users()
    # print(f'{user_ls=}')
    # user_detail = get_user_details(SAMPLE_USER)
    # print(f'{user_detail=}')
    # del_user(SAMPLE_USER)
    # users = get_users()
    # print(f'{users=}')
    # print(f'{get_user_details(TEST_USER_NAME)=}')
    # add_user(TEST_USER_NAME)


if __name__ == "__main__":
    main()

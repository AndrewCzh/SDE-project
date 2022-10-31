"""
This module encapsulates details about users.
"""
from pymongo import MongoClient
from bson.json_util import dumps

TEST_USER_NAME = 'Test user'
SAMPLE_USER = "Sample User"
NAME = 'name'
EMAIL = 'email'
FULL_NAME = 'full_name'

# We expect the user database to change frequently:
# For now, we will consider EMAIL to be
# our mandatory fields.
REQUIRED_FLDS = [NAME]
users = {TEST_USER_NAME: {EMAIL: 'x@y.com', FULL_NAME: 'Porgy Tirebiter'},
         'handle': {EMAIL: 'z@y.com', FULL_NAME: 'Nick Danger'}}
CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"
client = MongoClient(CONNECTION_STRING)
my_db = client["Users"]
my_col = my_db["Users"]


def user_exists(name):
    """
    Returns whether or not a user exists.
    """
    user = my_col.find_one({"name": name})  # return a cursor
    return user is not None


def get_users():
    user_ls = my_col.find({})
    ls = []
    for user in user_ls:
        ls.append(dumps(user))
    return ls


def get_user_details(name):
    user = my_col.find_one({"name": name})
    if user is not None:
        return user
    else:
        raise ValueError('User is not exist.')


def del_user(name):
    my_col.delete_one({'name': name})
    return


def add_user(name):
    # if not isinstance(name, str):
    #     raise TypeError(f'Wrong type for name: {type(name)=}')
    # if not isinstance(details, dict):
    #     raise TypeError(f'Wrong type for details: {type(details)=}')
    # for field in REQUIRED_FLDS:
    #     if field not in details:
    #         raise ValueError(f'Required {field=} missing from details')
    max_id = my_col.find().sort("u_id", -1).limit(1)
    uid = max_id[0]['u_id']+1
    # users[name] = details
    my_col.insert_one({'name': name, 'u_id': uid})


def main():
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

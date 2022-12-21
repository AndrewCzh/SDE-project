# from pymongo import MongoClient
# import check_correct_ingredients as cci
import db.db_connect as dbc


def add_up_money(uid, money):
    # connect to db
    dbc.connect_db()

    # check uid is in the db
    uid_filt = {'uid': uid}
    resp = dbc.fetch_one('Games', 'Games', uid_filt)
    if resp is not None:
        total_money = resp['money']
        total_money += money
        new_values = {"$set": {'money': total_money}}
        dbc.update_one('Games', 'Games', uid_filt, new_values)
        return 1
    else:
        print('uid is not in the database')
        return -1

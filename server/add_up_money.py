# from pymongo import MongoClient
# import check_correct_ingredients as cci
# import db.db_connect as dbc


def add_up_money(uid, money, uid_dict):
    # # connect to db
    # dbc.connect_db()
    #
    # # check uid is in the db
    # uid_filt = {'uid': uid}
    # resp = dbc.fetch_one('Games', 'Games', uid_filt)
    # if resp is not None:
    #     total_money = resp['money']
    #     total_money += money
    #     new_values = {"$set": {'money': total_money}}
    #     dbc.update_one('Games', 'Games', uid_filt, new_values)
    #     return 1
    # else:
    #     print('uid is not in the database')
    #     return -1
    if uid in uid_dict:
        uid_dict[uid] += money
        return 1
    else:
        print('uid is not in the uid_dict')
        return -1


def main():
    uid_dict = {'123': 110, '222': 10, 'test_uid': 0}
    ret = add_up_money('test_uid', 10, uid_dict)
    print(f'{ret=}')


if __name__ == '__main__':
    main()


"""
This module encapsulates details about food type.
"""
import db.db_connect as dbc

dbc.connect_db()
INGR = 'Ingredients'
NAME = 'name'


def get_food_types_dict(collection):
    ret = dbc.fetch_all_as_dict(collection, INGR, NAME)
    return ret


def get_food_types_list(collection):
    ret = dbc.fetch_all(collection, INGR)
    return ret


def get_food_type_details(collection, food):
    filt = {'name': food}
    ret = dbc.fetch_one(collection, INGR, filt)
    if ret is not None and '_id' in ret:
        del ret['_id']
        return ret
    else:
        return {'default_detail': 'default_value'}


def main():
    food_type = get_food_type_details('Burger', 'Bread')
    print(f'{food_type=}')


if __name__ == '__main__':
    main()

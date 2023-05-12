import sys
import pytest

sys.path.append("..")
import db.food_types as ftyp
import db.db_connect as dbc
dbc.connect_db()
COLLECTION = 'Burger'
BREAD = 'Bread'


@pytest.fixture(scope='function')
def new_food_type():
    dbc.insert_one(COLLECTION, ftyp.INGR, {'name': BREAD, 'price': 7.0})
    yield
    dbc.delete_one(COLLECTION, ftyp.INGR, {{'name': BREAD, 'price': 7.0}})


def test_get_food_types():
    ft = ftyp.get_food_types_list(COLLECTION)
    assert isinstance(ft, list)
    assert len(ft) >= 0
    if len(ft) > 0:
        assert len(ft) >= 1


def test_get_food_type_details():
    ftd = ftyp.get_food_type_details(COLLECTION, BREAD)
    assert isinstance(ftd, dict)


@pytest.mark.skip("Can't run this test untill the delete function is written.")
def test_del_food_type():
    assert False
    pass
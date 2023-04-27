import sys
import pytest

sys.path.append("..")
import db.food_types as ftyp
import db.db_connect as dbc
dbc.connect_db()
colletion = 'Burger'


def test_get_food_types():
    ft = ftyp.get_food_types_list(colletion)
    assert isinstance(ft, list)
    assert len(ft) > 1


def test_get_food_type_details():
    ftd = ftyp.get_food_type_details('PokeBowl', ftyp.AVOCADO)
    assert isinstance(ftd, dict)


@pytest.mark.skip("Can't run this test untill the delete function is written.")
def test_del_food_type():
    assert False
    pass
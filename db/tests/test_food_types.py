import sys

sys.path.append("..")
import db.food_types as ftyp


def test_get_food_types():
    ft = ftyp.get_food_types()
    assert isinstance(ft, list)
    assert len(ft) > 1


def test_get_food_type_details():
    ftd = ftyp.get_food_type_details(ftyp.AVOCADO)
    assert isinstance(ftd, dict)


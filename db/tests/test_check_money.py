import sys

sys.path.append("..")
import db.check_money as cm


def test_get_money_types():
    ct = cm.get_money_types()
    assert isinstance(ct, int)


def test_check_money():
    ret = cm.check_money()
    assert isinstance(ret, bool)

import sys
import pytest

sys.path.append("..")
import db.check_tool as ct


def test_get_tool_types():
    ft = ct.get_tool_types()
    assert isinstance(ft, list)
    assert len(ft) > 1


def test_get_tool_type_details():
    ftd = ct.get_tool_type_details(ct.GRILL)
    assert isinstance(ftd, dict)

@pytest.mark.skip()

def test_del_tool_type():
    pass
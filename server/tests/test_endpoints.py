import pytest

import sys

sys.path.append("..")
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

TEST_CHAR_TYPE = 'Warrior'


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


def test_get_character_type_list():
    """
    See if we can get a charcter type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.CHAR_TYPE_LIST).get_json()
    assert isinstance(resp_json[ep.CHAR_TYPE_LIST_NM], list)


def test_get_character_type_list_not_empty():
    """
    See if we can get a charcter type list properly.
    Return should look like:
        {CHAR_TYPE_LIST_NM: [list of chars types...]}
    """
    resp_json = TEST_CLIENT.get(ep.CHAR_TYPE_LIST).get_json()
    assert len(resp_json[ep.CHAR_TYPE_LIST_NM]) > 0


def test_get_character_type_details():
    """
    """
    resp_json = TEST_CLIENT.get(f'{ep.CHAR_TYPE_DETAILS}/{TEST_CHAR_TYPE}').get_json()
    assert TEST_CHAR_TYPE in resp_json
    assert isinstance(resp_json[TEST_CHAR_TYPE], dict)

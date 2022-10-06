import pytest

import sys

sys.path.append("..")
import server.endpoints as ep


TEST_CLIENT = ep.app.test_client()

TEST_CHAR_TYPE = 'Warrior'
TEST_FOOD_TYPE = 'Avocado'


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


def test_get_food_type_list():
    """
    See if we can get a food type list properly.
    Return should look like:
        {FOOD_TYPE_LIST_NM: [list of food types...]}
    """
    resp_json = TEST_CLIENT.get(ep.FOOD_TYPE_LIST).get_json()
    assert isinstance(resp_json[ep.FOOD_TYPE_LIST_NM], list)


def test_get_food_type_details():
    """
    See if we can get a food type properly
    Return should look like:
        {FOOD_TYPE_LIST_NM: {'price': 1}
    """
    resp_json = TEST_CLIENT.get(f'{ep.FOOD_TYPE_DETAILS}/{TEST_FOOD_TYPE}').get_json()
    assert TEST_FOOD_TYPE in resp_json
    assert isinstance(resp_json[TEST_FOOD_TYPE], dict)


def test_get_ingredients_generator_list():
    resp_json = TEST_CLIENT.get(ep.INGREDIENTS_GENERATOR_LIST).get_json()
    assert isinstance(resp_json[ep.INGREDIENTS_GENERATOR_LIST_NM], list)

import pytest
import sys

sys.path.append("..")
import db.db_connect as dbc
import db.users as usr
import server.endpoints as ep


TEST_CLIENT = ep.app.test_client()

TEST_FOOD_TYPE = 'Avocado'


def test_hello():
    """
    See if Hello works.
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


SAMPLE_USER_NM = 'Sample User'
SAMPLE_UID_NM = '5e4175d6-0d25-4e18-80c3-62014b9c1ab7'
SAMPLE_USER = {
    usr.NAME: SAMPLE_USER_NM,
    # usr.EMAIL: 'x@y.com',
    # usr.FULL_NAME: 'Sample User',
}
SAMPLE_UID = {
    usr.UID: SAMPLE_UID_NM,
    # usr.EMAIL: 'x@y.com',
    # usr.FULL_NAME: 'Sample User',
}


def test_add_user():
    """
    Test adding a user.
    """
    resp_json = TEST_CLIENT.post(ep.USER_ADD, json=SAMPLE_USER).get_json()
    assert usr.user_exists(resp_json[ep.USER_ADD_NM], SAMPLE_USER_NM)
    usr.del_user(SAMPLE_USER_NM)


def test_del_user():
    """
    Test deleting a user
    """
    TEST_CLIENT.post(ep.USER_ADD, json=SAMPLE_USER)
    usr.del_user(SAMPLE_UID_NM)
    resp_json = TEST_CLIENT.delete(ep.USER_DELETE, json=SAMPLE_UID).get_json()
    assert not usr.user_exists(resp_json[ep.USER_DELETE_NM], SAMPLE_USER_NM)


def test_get_user_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.USER_LIST)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.USER_LIST_NM], list)


def test_get_user_details():
    """
    See if we can get a valid user's details
    """
    resp_json = TEST_CLIENT.get(ep.USER_DETAILS).get_json()
    assert isinstance(resp_json[ep.USER_DETAILS_NM], dict)


# def test_get_character_type_list():
#     """
#     See if we can get a charcter type list properly.
#     Return should look like:
#         {CHAR_TYPE_LIST_NM: [list of chars types...]}
#     """
#     resp_json = TEST_CLIENT.get(ep.CHAR_TYPE_LIST).get_json()
#     assert isinstance(resp_json[ep.CHAR_TYPE_LIST_NM], list)
#
#
# def test_get_character_type_list_not_empty():
#     """
#     See if we can get a charcter type list properly.
#     Return should look like:
#         {CHAR_TYPE_LIST_NM: [list of chars types...]}
#     """
#     resp_json = TEST_CLIENT.get(ep.CHAR_TYPE_LIST).get_json()
#     assert len(resp_json[ep.CHAR_TYPE_LIST_NM]) > 0
#
#
# def test_get_character_type_details():
#     """
#     """
#     resp_json = TEST_CLIENT.get(f'{ep.CHAR_TYPE_DETAILS}/{TEST_CHAR_TYPE}').get_json()
#     assert TEST_CHAR_TYPE in resp_json
#     assert isinstance(resp_json[TEST_CHAR_TYPE], dict)

@pytest.fixture(scope='function')
def a_user():
    ret = usr.add_user(SAMPLE_USER_NM)
    yield ret
    usr.del_user(ret)


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


def test_get_ingredient_generator_details():
    resp_json = TEST_CLIENT.get(ep.INGREDIENTS_GENERATOR_DETAILS).get_json()
    assert isinstance(resp_json[ep.INGREDIENTS_GENERATOR_DETAIL_NM], list)


def test_start_game():
    resp_json = TEST_CLIENT.post(ep.NEW_GAME, json=SAMPLE_UID).get_json()
    assert isinstance(resp_json[ep.NEW_GAME_NM], str)
    document = ({"u_id": SAMPLE_UID['u_id'],
                 'game': resp_json[ep.NEW_GAME_NM]})
    dbc.delete_one('Games', 'Games', document)

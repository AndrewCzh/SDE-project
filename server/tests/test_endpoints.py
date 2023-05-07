import pytest
import sys
from unittest.mock import patch
from http import HTTPStatus

sys.path.append("..")
import db.db_connect as dbc
import db.users as usr
import db.games as ga
import server.endpoints as ep
import server.start_game as sg


TEST_CLIENT = ep.app.test_client()

TEST_FOOD_TYPE = 'Burger'
TEST_INGR_TYPE = 'Bread'
SAMPLE_USER_NM = 'Sample User'
SAMPLE_UID_NM = '5e4175d6-0d25-4e18-80c3-62014b9c1ab7'
RET_UID_NM = "3bf4bcca-313c-4917-ab89-6a08405f281d"
SAMPLE_USER = {
    usr.NAME: SAMPLE_USER_NM,
    usr.PASSWORD: '12345',
    # usr.EMAIL: 'x@y.com',
    # usr.FULL_NAME: 'Sample User',
}
SAMPLE_UID = {
    usr.UID: SAMPLE_UID_NM,
    # usr.EMAIL: 'x@y.com',
    # usr.FULL_NAME: 'Sample User',
}
SAMPLE_START = {
    sg.UID: "111cdb65-62a8-4df4-b958-550b2921fa86",
    sg.GID: "111cdb65-62a8-4df4-b958-550b2921fa87",
    # usr.EMAIL: 'x@y.com',
    # usr.FULL_NAME: 'Sample User',
}
RET_UID_DETAILS = {
    usr.UID: RET_UID_NM,
    usr.NAME: SAMPLE_USER_NM
}

RET_USER_COUNT = {
    usr.CNT: usr.count_user()
}
RET_GAME_COUNT = {
    ga.CNT: ga.count_game()
}

@pytest.fixture(scope='function')
def a_user():
    ret = usr.add_user(SAMPLE_USER_NM)
    yield ret
    usr.del_user(ret)


def test_add_user():
    """
    Test adding a user.
    """
    resp_json = TEST_CLIENT.post(ep.USER_ADD_W_NS, json=SAMPLE_USER).get_json()
    assert usr.user_exists(resp_json[ep.USER_ADD_NM], SAMPLE_USER_NM)
    usr.del_user(SAMPLE_USER_NM)


def test_del_user():
    """
    Test deleting a user
    """
    TEST_CLIENT.post(ep.USER_ADD_W_NS, json=SAMPLE_USER)
    usr.del_user(SAMPLE_UID_NM)
    resp_json = TEST_CLIENT.delete(ep.USER_DELETE_W_NS, json=SAMPLE_UID).get_json()
    assert not usr.user_exists(resp_json[ep.USER_DELETE_NM], SAMPLE_USER_NM)


def test_get_user_dict():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.USER_DICT_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.USER_DICT_NM], dict)


def test_get_user_list():
    """
    See if we can get a user list properly.
    Return should look like:
        {USER_LIST_NM: [list of users types...]}
    """
    resp = TEST_CLIENT.get(ep.USER_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.USER_LIST_NM], list)


@patch('db.games.get_games', return_value=None)
def test_get_game_list():
    """
    See if we can get a game list properly.
    Return should look like:
        {GAME_LIST_NM: [list of games...]}
    """
    resp = TEST_CLIENT.get(ep.GAMES_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.GAMES_LIST_NM], list)


@patch('db.users.count_user', return_value=RET_USER_COUNT, autospec=True)
def test_count_user(mock_count_user):
    """
    See if we can get the number of user properly
    """
    resp = TEST_CLIENT.get(f'{ep.USER_COUNT_W_NS}')
    assert resp.status_code == HTTPStatus.OK
    assert isinstance(resp.json[ep.USER_COUNT_NM], dict)
    assert usr.CNT in resp.json[ep.USER_COUNT_NM]


@patch('db.games.count_game', return_value=RET_GAME_COUNT, autospec=True)
def test_count_game(mock_count_game):
    """
    See if we can get the number of game properly
    """
    resp = TEST_CLIENT.get(f'{ep.GAME_COUNT_W_NS}')
    assert resp.status_code == HTTPStatus.OK
    assert isinstance(resp.json[ep.GAME_COUNT_NM], dict)
    assert ga.CNT in resp.json[ep.GAME_COUNT_NM]


@patch('db.users.get_user_details', return_value=RET_UID_DETAILS, autospec=True)
def test_get_user_details(mock_get_user_details):
    """
    See if we can get a valid user's details
    """
    resp = TEST_CLIENT.get(f'{ep.USER_DETAILS_W_NS}/{RET_UID_NM}')
    assert resp.status_code == HTTPStatus.OK
    # assert isinstance(resp.json, dict)
    assert isinstance(resp.json[ep.USER_DETAILS_NM], dict)
    assert usr.NAME in resp.json[ep.USER_DETAILS_NM]
    assert RET_UID_NM == resp.json[ep.USER_DETAILS_NM][usr.UID]


@patch('db.users.get_user_details', return_value=None, autospec=True)
def test_get_user_details_no_in_db(mock_get_user_details):
    """
    See if we can get a valid user's details
    """
    resp = TEST_CLIENT.get(f'{ep.USER_DETAILS_W_NS}/UID_NOT_IN_DB')
    assert resp.status_code == HTTPStatus.NOT_FOUND


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


def test_get_food_type_list():
    """
    See if we can get a food type list properly.
    Return should look like:
        {FOOD_TYPE_LIST_NM: [list of food types...]}
    """
    resp_json = TEST_CLIENT.get(f'{ep.FOOD_TYPE_LIST}/{TEST_FOOD_TYPE}').get_json()
    assert isinstance(resp_json[ep.FOOD_TYPE_LIST_NM], list)


def test_get_food_type_details():
    """
    See if we can get a food type properly
    Return should look like:
        {FOOD_TYPE_LIST_NM: {'price': 1}
    """
    resp_json = TEST_CLIENT.get(f'{ep.FOOD_TYPE_DETAILS}/{TEST_INGR_TYPE}/{TEST_FOOD_TYPE}').get_json()
    assert TEST_INGR_TYPE in resp_json
    assert isinstance(resp_json[TEST_INGR_TYPE], dict)


def test_get_game_list():
    """
    See if we can get a game list properly.
    Return should look like:
        {GAMES_LIST_NM: [list of games]}
    """
    resp = TEST_CLIENT.get(ep.GAMES_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.GAMES_LIST_NM], list)


def test_get_ingredient_generator_details():
    resp_json = TEST_CLIENT.get(ep.INGREDIENTS_GENERATOR_DETAILS).get_json()
    assert isinstance(resp_json[ep.INGREDIENTS_GENERATOR_DETAIL_NM], list)


def test_start_game():
    resp_json = TEST_CLIENT.post(f'{ep.GAMES_NS}{ep.NEW_GAME}', json=SAMPLE_START).get_json()
    assert isinstance(resp_json[ep.NEW_GAME_NM], str)
    document = ({"u_id": SAMPLE_START['uid'],
                 'game': SAMPLE_START['gid']})
    dbc.delete_one('Games', 'Games', document)

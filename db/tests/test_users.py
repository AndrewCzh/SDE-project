import pytest
import sys

sys.path.append("..")
import db.users as usr
# import db.db_connect as dbc


@pytest.fixture(scope='function')
def new_user_type():
    global uid
    uid = usr.add_user(usr.TEST_USER_NAME, usr.TEST_PASSWORD)
    yield
    usr.del_user(uid)


def test_get_users():
    usrs = usr.get_users()
    assert isinstance(usrs, list)
    assert len(usrs) >= 0


def test_get_user_details(new_user_type):
    # usr_details = usr.get_user_details(usr.TEST_UID)
    usr_details = usr.get_user_details(uid)
    assert isinstance(usr_details, dict)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        usr.add_user(7)
#
#
# def test_add_wrong_details_type():
#     with pytest.raises(TypeError):
#         usr.add_user('a new user', [])
#
#
# def test_add_missing_field():
#     with pytest.raises(ValueError):
#         usr.add_user('a new user', {'foo': 'bar'})


def test_add_user():
    # details = {}
    # for field in usr.REQUIRED_FLDS:
    #     details[field] = 2
    # uid = usr.add_user("Sample User")
    uid = usr.add_user(usr.TEST_USER_NAME, usr.TEST_PASSWORD)
    # usr.add_user(usr.TEST_USER_NAME, details)
    assert usr.user_exists(uid, usr.TEST_USER_NAME)
    usr.del_user(uid)


# @pytest.mark.skip("Can't run this test untill the delete function is written.")
def test_del_user():
    uid = usr.add_user(usr.TEST_USER_NAME, usr.TEST_PASSWORD)
    # usr.add_user(usr.TEST_USER_NAME, details)
    assert usr.user_exists(uid, usr.TEST_USER_NAME)
    usr.del_user(uid)
    assert not usr.user_exists(uid, usr.TEST_USER_NAME)


def test_count_user():
    cnt = usr.count_user()
    assert isinstance(cnt, int)
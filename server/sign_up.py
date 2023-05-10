import db.db_connect as dbc
import uuid
from server.login import app

USER = 'Users'
username = 'A New User#00001'
password = '123456'


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    dbc.connect_db()
    username_filt = ({'name': username})
    if dbc.fetch_one(USER, USER, username_filt):
        print("Username already exists")
    else:
        uid = str(uuid.uuid4())
        insert_filt = ({'uid': uid, 'name': username, 'password': password})
        dbc.insert_one(USER, USER, insert_filt)
        print("Insert successfully")


def main():
    sign_up()


if __name__ == '__main__':
    main()

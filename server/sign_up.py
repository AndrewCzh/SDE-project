import db.db_connect as dbc
# from flask import Flask, render_template, request, session
import uuid
from server.login import app

USER = 'Users'
username = 'A New User#00001'
password = '123456'


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    dbc.connect_db()
    # username = request.form['username']
    # password = request.form['password']
    username_filt = ({'name': username})
    if dbc.fetch_one(USER, USER, username_filt):
        # render_template('signup.html', error="Username already exists")
        print("Username already exists")
    else:
        uid = str(uuid.uuid4())
        insert_filt = ({'uid': uid, 'name': username, 'password': password})
        dbc.insert_one(USER, USER, insert_filt)
        print("Insert successfully")
        # uid_filt = ({'uid': uid})
        # if dbc.fetch_one(USER, USER, uid_filt):
        #     dbc.delete_one(USER, USER, uid_filt)
        #     if dbc.fetch_one(USER, USER, uid_filt) is None:
        #         print("Delete successfully")

        # render_template('login.html')


def main():
    sign_up()


if __name__ == '__main__':
    main()

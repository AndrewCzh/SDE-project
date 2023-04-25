# from pymongo import MongoClient
import uuid
# from bson.json_util import dumps
# import random
# import jsonify
from flask import Flask, render_template, request, session, redirect, url_for
# import ingredients_generator as ig
# session, url_for, redirect
import db.db_connect as dbc
import start_game as sg
from bson.json_util import loads
import check_correct_ingredients as cci

USER = 'Users'
GAMES = 'Games'

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        dbc.connect_db()
        username = request.form['username']
        password = request.form['password']
        password_two = request.form['passwordtwo']
        if password != password_two:
            error = 'The second entry of your password\
            does not match the previous one'
            return render_template('signup.html', error=error)

        # data = "get usernames from db"
        # check username's uniqueness
        unique_filt = ({'name': username})
        unique = dbc.fetch_one(USER, USER, unique_filt)
        if unique:
            error = "This username already exists."
            return render_template('signup.html', error=error)
        else:
            # add new account to db
            uid = str(uuid.uuid4())
            document = ({'u_id': uid, 'name': username, 'password': password})
            dbc.insert_one(USER, USER, document)
            return render_template('login.html')
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login_auth():
    """
    These comments are used to connect db
    """
    if request.method == 'POST':
        dbc.connect_db()

        username = request.form['username']
        session['username'] = username

        password = request.form['password']

        # check authentication
        auth_filt = ({'name': username, 'password': password})
        auth = dbc.fetch_one(USER, USER, auth_filt)
        print(f'{auth=}')
        if auth:
            uid = auth['u_id']
            session['uid'] = uid
            # return render_template('menu.html')
            # still need to insert to db for time checking
            uid = str(uuid.uuid4())
            document = ({'u_id': uid, 'name': username, 'password': password})
            dbc.insert_one(USER, USER, document)
            return redirect(url_for('menu'))
        else:
            return render_template('login.html', error="Password is wrong")
    else:
        return render_template('login.html')
# @app.route('/cook', methods=['POST'])
# def check_correct_ingredients():
#     print("check start")
#     print(request.form)
#
#     print(request.form.get('beef'))
#     for key, val in request.form.items():
#         print(key, val)
#     return render_template('success.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    print("inside menu")
    # uid = session['uid']
    # gid = str(uuid.uuid4())
    # session['gid'] = gid
    # data_ls, oid, game_id = sg.start_game(uid, gid)
    # session['oid'] = oid
    session['money'] = 0
    print(f'{session["money"]=}')
    gid = str(uuid.uuid4())
    session['gid'] = gid
    return render_template('menu.html')


def get_user_data(uid):
    user = dbc.fetch_one(USER, USER, {'u_id': uid})
    if user:
        return user
    else:
        return None


def get_game_times(username):
    game_times = dbc.count(USER, USER, {'name': username})
    return game_times


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    uid = session['uid']
    username = session['username']
    user = get_user_data(uid)
    if user:
        # TODO: retrieve highest score from database
        highest_score = 0
        game_times = get_game_times(username) - 2
        return render_template('profile.html', username=username,
                               highest_score=highest_score,
                               game_times=game_times)
    else:
        error = "User not found"
        return render_template('error.html', error=error)


@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    needs to receive a fixed target to pass the level,
    the current money amount, and timer info
    """
    money = 0
    target = 1000
    timeout = False
    error = "ERROR"

    if timeout:
        if money < target:
            return render_template('success.html', error=error)
        else:
            return render_template('failed.html', error=error)

    uid = session['uid']
    gid = session['gid']
    data_ls, oid, game_id = sg.start_game(uid, gid)
    session['oid'] = oid
    print(f"inside home: {session['oid']=}, {session['gid']=}")
    return render_template('home.html', data_ls=data_ls)


# receiving selected ingredients from home.html
@app.route('/ProcessUserinfo/<string:list>', methods=['POST'])
def ProcessUserinfo(list):
    print(f"inside Process: {list=}")
    session.modified = True
    session['ing'] = list
    return redirect(url_for('success'))


@app.route('/cook', methods=['GET', 'POST'])
def cooking():
    # money += cci.check_correct_ingredients(session['ing'],
    #                                        session['gid'], session['oid'])
    print(f"{session['money']=}")
    # selected_cook
    # correct_cook
    # if selected_cook == correct_cook:
    #     return "cooking animation"
    # else:
    #     return render_template('failed.html')
    data = session.get('ing')
    print(f'Inside cook : {data}')
    data = loads(data)
    print(f"{type(data)=}, {data=}")
    print(f"inside cook: {session['oid']=}, {session['gid']=}")
    money = cci.check_correct_ingredients(data,
                                          session['gid'], session['oid'])
    print(f"{money=}")
    print(f"before adding, {session['money']=}")
    session['money'] = session.get('money') + money
    print(f"{session['money']=}")
    return render_template('cook1.html')


@app.route('/success')
def success():

    # return redirect(url_for('menu'))
    return render_template('success.html')


@app.route('/failed')
def failed():

    return render_template('failed.html')


def main():

    # print(login())
    app.run(debug=True)


if __name__ == "__main__":
    main()

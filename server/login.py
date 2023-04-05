# from pymongo import MongoClient
import uuid
# from bson.json_util import dumps
# import random
import jsonify
from flask import Flask, render_template, request, session
# import ingredients_generator as ig
# session, url_for, redirect
import db.db_connect as dbc
import start_game as sg

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
        # TODO waiting frontend page to be connected

        password = request.form['password']

        # check authentication
        auth_filt = ({'name': username, 'password': password})
        auth = dbc.fetch_one(USER, USER, auth_filt)
        print(f'{auth=}')
        if 'name' in auth:
            uid = auth['u_id']
            session['uid'] = uid
            render_template('menu.html')
        else:
            error = "password is wrong"
            render_template('login.html', error=error)
    else:
        return render_template('login.html')

    insert = True
    # if data is None:
    #     u_id = 0
    # else:
    #     u_id = 0
    #     for user in data:
    #         if user['name'] == username:
    #             insert = False
    #             break
    #         u_id = max(u_id, user['u_id'])
    if insert:
        print("here1")
        """
        These comments are used to connect db
        """
        # check if uid is already in the users table
        uid = 0
        found = 1
        while found:
            uid = str(uuid.uuid4())
            found = dbc.fetch_one(USER, USER, ({'u_id': uid}))
        document = ({'u_id': uid, 'name': username, 'password': password})
        dbc.insert_one(USER, USER, document)
        # my_col.insert_one(document)
        session['uid'] = uid
        print(username, uid)
        print('here2')
        # TODO delete this after creating start_game.html
        # data_ls = sg.start_game(uid)[0]
        # data_ls = ig.generator(uid, '')
        # return render_template('home.html')
        # return ig.generator(uid)
        # return redirect(url_for('home'))
        return render_template('menu.html')
        # change to menu.html
    else:
        error = "name is already used"
        # return render_template('login.html', error=error)
        render_template('menu.html', error=error)

# @app.route('/cook', methods=['POST'])
# def check_correct_ingredients():
#     print("check start")
#     print(request.form)
#
#     print(request.form.get('beef'))
#     for key, val in request.form.items():
#         print(key, val)
#     return render_template('success.html')


@app.route('/home', methods=['GET', 'POST'])
def menu():
    uid = session['uid']
    data_ls = sg.start_game(uid)[0]
    return render_template('home.html', data_ls=data_ls)


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
        game_times = get_game_times(username) - 1
        return render_template('profile.html', username=username,
                               highest_score=highest_score,
                               game_times=game_times)
    else:
        error = "User not found"
        return render_template('error.html', error=error)


@app.route('/cook', methods=['GET', 'POST'])
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

    # selected_ing
    # correct_ing
    # if selected_ing != correct_ing:
    #     price_earned = price * 0.8
    return render_template('cook.html')


@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    # You can now use the data in your Flask application
    print(data)
    return jsonify({'status': 'success'})


@app.route('/cook', methods=['GET', 'POST'])
def cooking():
    # selected_cook
    # correct_cook
    # if selected_cook == correct_cook:
    #     return "cooking animation"
    # else:
    #     return render_template('failed.html')
    return render_template('cook.html')


@app.route('/success')
def success():
    return render_template('menu.html')


@app.route('/failed')
def failed():
    return render_template('login.html')


def main():

    # print(login())
    app.run(debug=True)


if __name__ == "__main__":
    main()

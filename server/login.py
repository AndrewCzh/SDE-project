from pymongo import MongoClient
import uuid
# from bson.json_util import dumps
# import random
import jsonify
from flask import Flask, render_template, request
# import ingredients_generator as ig
# session, url_for, redirect
import db.db_connect as dbc
import start_game as sg

app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login_auth():
    """
    These comments are used to connect db
    """
    dbc.connect_db()

    username = request.form['username']
    client = MongoClient(CONNECTION_STRING)
    my_db = client["Users"]
    my_col = my_db["Users"]

    # data = my_col.find()
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
            found = my_col.find_one({'u_id': uid})
        document = ({'u_id': uid, 'name': username})
        my_col.insert_one(document)
        print(username, uid)
        print('here2')
        # TODO delete this after creating start_game.html
        data_ls = sg.start_game(uid)[0]
        # data_ls = ig.generator(uid, '')
        # return render_template('home.html')
        # return ig.generator(uid)
        # return redirect(url_for('home'))
        return render_template('home.html', data_ls=data_ls)   
        # change to menu.html
    else:
        error = "name is already used"
        # return render_template('login.html', error=error)
        render_template('login.html', error=error)

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
    return render_template('home.html')


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
    return render_template('login.html')


@app.route('/failed')
def failed():
    return render_template('login.html')


def main():
    # print(login())
    app.run(debug=True)


if __name__ == "__main__":
    main()

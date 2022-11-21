from pymongo import MongoClient
import uuid
# from bson.json_util import dumps
# import random
# import json
from flask import Flask, render_template, request
import ingredients_generator as ig
# session, url_for, redirect
import yaml

app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


# with open("/Users/jialixu/Documents/GitHub/SDE-project/.github/workflows/main.yml") as file:
#     try:
#         doc = yaml.safe_load(file)
#         CONNECTION_STRING = doc['env']['CONNECTION_STRING']
#         print(CONNECTION_STRING)
#     except:
#         print("FAILED")


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def login_auth():
    """
    These comments are used to connect db
    """
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

        # return render_template('home.html')
        return ig.generator(uid)
        # return redirect(url_for('home'))
    else:
        error = "name is already used"
        return render_template('login.html', error=error)


# @app.route('/cook', methods=['POST'])
# def check_correct_ingredients():
#     print("check start")
#     print(request.form)
#
#     print(request.form.get('beef'))
#     for key, val in request.form.items():
#         print(key, val)
#     return render_template('success.html')


# @app.route('/home')
# def home():
#     return render_template('home.html')


@app.route('/cook', methods=['GET', 'POST'])
def cooking():
    return render_template('cook.html')


def main():
    # print(login())
    app.run(debug=True)


if __name__ == "__main__":
    main()

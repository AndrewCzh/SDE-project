# from pymongo import MongoClient
# from bson.json_util import dumps
# import random
# import json
from flask import Flask, render_template, request
import ingredients_generator as ig
# session, url_for, redirect

app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def login_auth():
    """
    These comments are used to connect db
    """
    username = request.form['username']
    # client = MongoClient(CONNECTION_STRING)
    # my_db = client["Users"]
    # my_col = my_db["Users"]
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
        # document = ({'u_id': u_id+1, 'name': username})
        # my_col.insert_one(document)
        print(username)
        print('here2')

        # return render_template('home.html')
        return ig.generator()
        # return redirect(url_for('home'))
    else:
        error = "name is already used"
        return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html')
    

def main():
    # print(login())
    app.run(debug=True)


if __name__ == "__main__":
    main()

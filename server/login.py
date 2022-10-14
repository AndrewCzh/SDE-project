from pymongo import MongoClient
# from bson.json_util import dumps
# import random
import json
from flask import Flask, render_template, request, session, url_for, redirect, jsonify

app = Flask(__name__)

# CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
# cluster0.wnpabny.mongodb.net/Ingredients"
#
#
# client = MongoClient(CONNECTION_STRING)


# @app.route('/')
# def index():
#     return jsonify({'name': 'alice', 'email': 'alice@gmail.com'})


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/loginAuth', methods=["POST"])
def login():
    username = request.form['username']
    print(username)
    print('here')
    return render_template('home.html')
    # return redirect(url_for('home'))


def main():
    # print(login())
    app.run(debug=True)


if __name__ == "__main__":
    main()

from pymongo import MongoClient
from flask import Flask, render_template, request

app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"

@app.route('/')
def index():
    return render_template('cook.html')


@app.route('/cook')
def home():
    return render_template('success.html')


@app.route('/cook')
def home():
    return render_template('fail.html')

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
from flask import Flask, render_template
from db import db_connect as dbc

app = Flask(__name__)


CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@\
cluster0.wnpabny.mongodb.net/Ingredients"


@app.route('/')
def cook():
    return render_template('cook.html')


@app.route('/cookSuccess')
def cookSuccess():
    return render_template('success.html')


@app.route('/cookFailed')
def cookFailed():
    return render_template('fail.html')


@app.route('/login', methods=['GET', 'POST'])


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()

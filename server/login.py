import uuid
import jsonify
from flask import Flask, render_template, request, session, redirect, url_for
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
            document = ({'u_id': uid, 'name': username,
                         'password': password, 'times': 0})
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
            times = auth['times'] \
                if 'times' in auth else 0
            print(f'{times=}')
            times += 1
            dbc.update_one(USER, USER, {'u_id': uid},
                           {'$set': {'times': times}})
            return redirect(url_for('menu'))
        else:
            return render_template('login.html', error="Password is wrong")
    else:
        return render_template('login.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    print("inside menu")
    money = 0
    session['money'] = money
    print(f'{session["money"]=}')
    gid = str(uuid.uuid4())
    session['gid'] = gid
    return render_template('menu.html')


def get_user_data(uid, name):
    user = dbc.fetch_one(USER, USER, {'u_id': uid, 'name': name})
    if user:
        times = user['times'] if 'times' in user else -1
        highest_score = user['highest_score'] if 'highest_score' in user else 0
        return times, highest_score
    else:
        return None


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    uid = session['uid']
    username = session['username']
    user = get_user_data(uid, username)
    if user:
        # retrieve highest score from database
        highest_score = user[1]
        game_times = user[0]
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
    money = session['money']
    target = 150
    timeout = False
    error = "ERROR"
    dish = 'SALAD'
    if timeout:
        if money < target:
            return render_template('success.html', error=error)
        else:
            return render_template('failed.html', error=error)

    uid = session['uid']
    gid = session['gid']
    data_ls, oid, game_id = sg.start_game(uid, gid)
    print(f'{data_ls=}')
    if "Rice" in data_ls[1]:
        dish = 'SUSHI'
    elif "Crust" in data_ls[1]:
        dish = 'PIZZA'
    elif "Bread" in data_ls[1]:
        dish = 'BURGER'

    session['oid'] = oid
    session['generated_order'] = data_ls
    print(f"inside home: {session['oid']=}, {session['gid']=}")
    print(data_ls)
    return render_template('home.html', data_ls=data_ls,
                           money=money, dish=dish)


@app.route('/my_python_script', methods=['POST'])
def my_python_script():
    data = request.get_json()
    myBoolean = data['myBoolean']
    print("BOOLEAN: ", myBoolean)
    return jsonify(success=True)


# receiving selected ingredients from home.html
@app.route('/ProcessUserinfo/<string:list>', methods=['POST'])
def ProcessUserinfo(list):
    print(f"inside Process ingredients: {list=}")
    session.modified = True
    session['ing'] = list
    return redirect(url_for('success'))


@app.route('/ProcessToolinfo/<string:list>', methods=['POST'])
def ProcessToolinfo(list):
    print(f"inside Process tool: {list=}")
    session.modified = True
    session['tool'] = list
    return redirect(url_for('success'))


@app.route('/cook', methods=['GET', 'POST'])
def cooking():
    print(f"{session['money']=}")
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
    return render_template('cook.html', money=session['money'])


def update_highest_score(uid, money):
    filt = {'u_id': uid}
    ret = dbc.fetch_one(USER, USER, filt)
    if ret:
        score = ret['highest_score'] if 'highest_score' in ret else 0
        if money > score:
            dbc.update_one(USER, USER, filt,
                           {'$set': {'highest_score': money}})
        else:
            pass


@app.route('/cookTool', methods=['GET', 'POST'])
def pickCookTool():
    print(f"{session['money']=}")
    data2 = session.get('tool')
    data2 = loads(data2)
    money2 = cci.check_correct_tool(data2,
                                    session['gid'], session['oid'])
    session['money'] = session.get('money') + money2
    return render_template('cook.html')


@app.route('/success')
def success():
    update_highest_score(session['uid'], session['money'])
    return render_template('success.html')


@app.route('/failed')
def failed():
    update_highest_score(session['uid'], session['money'])
    return render_template('failed.html')


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()

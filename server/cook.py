from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/done', methods=['POST'])  # to get user's selection for cooktools
def done():
    if request.method == 'POST':
        # Retrieve user's selection from the request
        # Oven = request.form['Oven']
        # RiceCooker = request.form['RiceCooker']
        # Grill = request.form['Grill']
        # Process the selection and return to earn point page
        render_template('earnings.html')
    else:
        return render_template('fail.html')


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
#
#
# if __name__ == "__main__":
#     main()

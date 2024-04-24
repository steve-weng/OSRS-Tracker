from flask import Flask
from flask import request, jsonify, render_template
import pandas as pd
import requests

app = Flask(__name__)

df1 = pd.read_pickle("ItemIDs.pkl")
filtered_df1 = df1.loc[df1['Name'].str.contains('JUST')]
print(filtered_df1)

from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt

app = Flask(__name__)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'this is a secret key '
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # is_active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return f'<User {self.username}>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('addItem'))
        
        else:
            return render_template('incorrect.html')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('registeration.html')


@app.route('/logout_page')
def logout_page():
    logout_user()
    return render_template('logout.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('logout_page'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)






@app.route('/addItem', methods=['GET', 'POST'])
def addItem(result=None):
    if request.args.get('itemID', None):
        result = searchItem(request.args['itemID'], request.args['amount'])
    
    itemList = list(df1['Name'])
    return render_template('main.html', result=result, items = itemList)


def process_text(text):
    return "FOO" + text


def searchItem(itemID, amount):

    # headers = {
    
    # 'User-Agent' : 'learning to make a price alert',
    # 'From': 'testing@gmail.com'
    # }


    # response = requests.get('https://prices.runescape.wiki/api/v1/osrs/5m', headers=headers)

    # if response.status_code == 200:
    #     #print ("connected")
    #     #print ("---------------------------------")
    #     data = response.json()
    # elif response.status_code == 404:
    #     return "unable to reach"
    # else:
    #     return "failed to connect"

    # double check the pickled file and table saved
    print(itemID)
    print(amount)
    itemRow = df1.loc[df1['Name'] == itemID]
    print(itemRow)
    itemIDNum = itemRow['itemID']
    itemIDNum = itemIDNum.iloc[0]
    print(itemIDNum)

    #itemData = data["data"][itemID]
    #if int(amount) <= itemData['avgHighPrice']:
    #    return "threshold " + amount + " is set.  Current high price is " + str(itemData['avgHighPrice']) + ".  Low is " + str(itemData['avgLowPrice'])
    #else:
    #    return itemData
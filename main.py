from flask import Flask
from flask import request, jsonify, render_template
import pandas as pd
import requests

app = Flask(__name__)

df1 = pd.read_pickle("ItemIDs.pkl")
filtered_df1 = df1.loc[df1['Name'].str.contains('JUST')]
print(filtered_df1)

@app.route('/', methods=['GET', 'POST'])
def index(result=None):
    if request.args.get('itemID', None):
        result = searchItem(request.args['itemID'], request.args['amount'])
    
    itemList = list(df1['Name'])
    return render_template('main.html', result=result, items = itemList)


def process_text(text):
    return "FOO" + text

@app.route('/index')
def hello():
    return render_template('index.html')


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
    df = pd.read_pickle("ItemIDs.pkl")
    filtered_df = df.loc[df['Name'].str.contains('JUST')]
    print(filtered_df)

    #itemData = data["data"][itemID]
    #if int(amount) <= itemData['avgHighPrice']:
    #    return "threshold " + amount + " is set.  Current high price is " + str(itemData['avgHighPrice']) + ".  Low is " + str(itemData['avgLowPrice'])
    #else:
    #    return itemData
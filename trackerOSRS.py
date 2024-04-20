import sqlite3
import requests


con = sqlite3.connect("test5.db")
cur = con.cursor()

#.execute("CREATE TABLE items(id,name, high_price, low_price)")

#res = cur.execute("SELECT name FROM sqlite_master")
#print(res.fetchone())

# test item, we'll get this from the front end
# itemID = "13190"
# itemName = "Old school bond"
# high_price = 1000 # and these from scraping the site
# low_price = 999

# cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", 
# 	(itemID, itemName, high_price, low_price))

# for row in cur.execute("SELECT * FROM items"):
# 	print(row)

headers = {
	
	'User-Agent' : 'learning to make a price alert',
	'From': 'testing@gmail.com'
}

response = requests.get('https://prices.runescape.wiki/api/v1/osrs/5m', headers=headers)
response = requests.get('https://static.runelite.net/api/runelite-api/net/runelite/api/ItemID.html')

if response.status_code == 200:
	print ("connected")
	print ("---------------------------------")
	data = response.json()
	#print(data)
elif response.status_code == 404:
	print ("unable to reach")
else:
	print ("failed to connect")

print (data)
#rint (type(data))
#itemData = data["data"]["2"]
#print(itemData)
#print(type(itemData)) # we want the data, and the second identifier is the item ID
# is a dict, so need to transform this dict into a table
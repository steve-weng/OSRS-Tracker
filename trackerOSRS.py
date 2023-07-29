import sqlite3

con = sqlite3.connect("test5.db")
cur = con.cursor()

cur.execute("CREATE TABLE items(id,name, high_price, low_price)")

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())

# test item, we'll get this from the front end
itemID = "13190"
itemName = "Old school bond"
high_price = 1000 # and these from scraping the site
low_price = 999

cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", 
	(itemID, itemName, high_price, low_price))

for row in cur.execute("SELECT * FROM items"):
	print(row)

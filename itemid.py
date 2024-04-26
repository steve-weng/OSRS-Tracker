### run this only if you need to update item ID or new items are released (that you want to track)
### it updates the pickle file with item IDs based off runelite's GE API

import pandas as pd

tables = pd.read_html('https://static.runelite.net/api/runelite-api/constant-values.html')
df = tables[9] #currently 9th table on this page is the itemID table
df = df.drop(columns=[0])
df = df.rename({1: "Name", 2:"itemID"}, axis = 'columns')
df.to_pickle("ItemIDs.pkl")

# double check the pickled file and table saved
df_unpickle = pd.read_pickle("ItemIDs.pkl")
print(df_unpickle)
import pandas as pd

#url = 'https://static.runelite.net/api/runelite-api/constant-values.html'
#url = 'https://static.runelite.net/api/runelite-api/net/runelite/api/ItemID.html'
url = 'https://static.runelite.net/api/runelite-api/constant-values.html#net.runelite.api.ItemID'

tables = pd.read_html('https://static.runelite.net/api/runelite-api/constant-values.html')
df = tables[9] #currently 9th table on this page is the itemID table

df.to_pickle("ItemIDs.pkl")

df_unpickle = pd.read_pickle("ItemIDs.pkl")

print(df_unpickle)







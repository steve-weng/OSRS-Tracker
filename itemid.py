import pandas as pd

tables = pd.read_html('https://static.runelite.net/api/runelite-api/constant-values.html')
df = tables[9] #currently 9th table on this page is the itemID table

df.to_pickle("ItemIDs.pkl")

# double check the pickled file and table saved
df_unpickle = pd.read_pickle("ItemIDs.pkl")
print(df_unpickle)
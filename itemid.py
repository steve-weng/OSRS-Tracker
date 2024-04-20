import pandas as pd
from bs4 import BeautifulSoup

import requests

url = 'https://static.runelite.net/api/runelite-api/constant-values.html'
r = requests.get(url)

if r.status_code == 200:
	print ("connected")
	print ("---------------------------------")
	data = r.text
	#print(data)
elif response.status_code == 404:
	print ("unable to reach")
else:
	print ("failed to connect")

soup = BeautifulSoup(data, "html.parser")
#tables = pd.read_html(str(soup))
#with open('saved.html', 'w') as f:
#	f.write(str(soup))

#print (soup)
#soupTR = soup.find_all('tr')
#with open('saved.html', 'w') as f:
#	f.write(str(soupTR))

soupTable = soup.find_all('table')
with open('s1.html', 'w') as f:
	f.write(str(soupTable[0]))

df = pd.read_html(str(soupTable[0]))
print(df)
# # Read the HTML file into a Pandas dataframe
# with open('https://static.runelite.net/api/runelite-api/constant-values.html') as file:
#     soup = BeautifulSoup(file, 'html.parser')
# tables = pd.read_html(str(soup))








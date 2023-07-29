import requests

headers = {
	
	'User-Agent' : 'learning to make a price alert',
	'From': 'steve.weng09175@gmail.com'
}

response = requests.get('https://prices.runescape.wiki/api/v1/osrs/5m', headers=headers)

if response.status_code == 200:
	print ("connected")
	print ("---------------------------------")
	data = response.json()
	print(data)
elif response.status_code == 404:
	print ("unable to reach")
else:
	print ("failed to connect")
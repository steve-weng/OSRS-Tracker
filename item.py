import pandas as pd
from bs4 import BeautifulSoup

import requests

url = 'https://static.runelite.net/api/runelite-api/constant-values.html'

dfs = pd.read_html(url)
display(dfs)
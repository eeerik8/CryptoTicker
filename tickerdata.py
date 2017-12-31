import urllib
import json
import requests

page = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/")
pre_json = page.read()
#fetch json file, read, and then load.
loaded_json_list = json.loads(pre_json)
#note that only the top 10 cryptocurrencies are going to be shown.
for x in range(10):
	current = loaded_json_list[x]
	print(current["name"])
	print(current["symbol"])
	print(current["price_usd"])
	print(current["rank"])
	print(current["percent_change_1h"])
	print(current["percent_change_24h"])

class crypto:
	symbol=""
	price_usd = 0.00
	rank = 0
	percent_change_24h = 0.00
	percent_change_1h =0.00
	def __init__(self,name,symbol, price_usd,rank,percent_change_1h, percent_change_24h):
		self.name = name
		self.symbol = symbol
		self.price_usd = price_usd
		self.rank = rank
		self.percent_change_24h = percent_change_24h
		self.percent_change_1h = percent_change_1h

def make_crypto
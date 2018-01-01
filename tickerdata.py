import urllib
import json
import requests

class Crypto(object):
	def __init__(self,name,symbol, price_usd,rank,percent_change_1h, percent_change_24h):
		self.name = name
		self.symbol = symbol
		self.price_usd = price_usd
		self.rank = rank
		self.percent_change_24h = percent_change_24h
		self.percent_change_1h = percent_change_1h
	def __repr__(self):
		rstring = self.rank + '. ' + self.name + ' (' + self.symbol + ') ' + self.price_usd + ' ' + self.percent_change_1h + ' ' + self.percent_change_24h + '\n'
		return rstring


page = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/")
pre_json = page.read()
#fetch json file, read, and then load.
loaded_json_list = json.loads(pre_json)
#note that only the top 10 cryptocurrencies are going to be shown.
currency =[]
for x in range(10):
	current = loaded_json_list[x]
	crypto_obj = Crypto(current["name"], current["symbol"], current["price_usd"], current["rank"], current["percent_change_1h"], current["percent_change_24h"])
	currency.append(crypto_obj)

#great, now we have objects in a list that we can call!
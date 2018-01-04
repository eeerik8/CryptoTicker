import urllib
import json
import requests

class Crypto(object):
	def __init__(self,name,symbol, price_usd,rank,percent_change_1h, percent_change_24h):
		self.name = name
		self.symbol = symbol
		self.price_usd = price_usd
		self.rank = rank
		if(float(percent_change_24h) > 0.00000):
			percent_change_24h = '+' + percent_change_24h
		if(float(percent_change_1h) > 0.00000):
			percent_change_1h = '+' + percent_change_1h
		self.percent_change_24h = percent_change_24h
		self.percent_change_1h = percent_change_1h
	def __repr__(self):
		rstring = self.rank + '. ' + self.name + ' (' + self.symbol + ') ' + self.price_usd + ' ' + self.percent_change_1h + ' ' + self.percent_change_24h + '\n'
		return rstring

def refresh():
	page  =requests.get("https://api.coinmarketcap.com/v1/ticker/")
	loaded_json_list = page.json()
	currency =[]
	for x in range(10):
		current = loaded_json_list[x]
		crypto_obj = Crypto(current["name"], current["symbol"], current["price_usd"], current["rank"], current["percent_change_1h"], current["percent_change_24h"])
		currency.append(crypto_obj)
	return currency
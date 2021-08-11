class Ticker(object):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def __repr__(self):
        return "[{0},{1}]".format(self.symbol, self.price)

def get_ticker(coin):
  with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/price?symbol="+coin+"USDT") as url:
    data = json.loads(url.read().decode())
    t = Ticker(**data)
    return t

import urllib.request, json 
import sqlite3
#** DB location **
dbLoc = '/home/ubuntu/binance-trade-bot/data/crypto_trading.db'
#*****************
#** Reference coin **
refCoin = "ETH"
#********************
conn = sqlite3.connect(dbLoc)
cursor = conn.execute("SELECT * from coin_value order by id DESC limit 10")
s0=[]
tkREF = get_ticker(refCoin)
acum = 0
for row in cursor:
  tkTemp = get_ticker(row[1])
  if s0.count(row[1])>=1:
    break
  if (float(tkTemp.price)*float(row[2])) >= 10 :  
    print (row[1])
    print ("Amount -> ", float(row[2]))
    print ("Ticker -> U$ ", tkTemp.price)
    print ("Balance -> U$ ",float(tkTemp.price)*float(row[2]))
    print (refCoin," equiv -> ",float(tkTemp.price)*float(row[2])/float(tkREF.price))
    print ("")
    acum = acum + float(tkTemp.price)*float(row[2])/float(tkREF.price)
  s0.append(row[1])
print ("Total ",refCoin," equiv -> ", acum)
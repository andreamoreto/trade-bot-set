import urllib.request, json 
import sqlite3
from datetime import datetime

dbLoc = '/home/ubuntu/binance-trade-bot/data/crypto_trading.db'
conn = sqlite3.connect(dbLoc)
sqlstr='''
select trade_history.*
from trade_history
where trade_history.rowid in (select t2.rowid
                  from trade_history t2
                  where t2.alt_coin_id = trade_history.alt_coin_id
                  order by datetime desc
                  limit 16
                 )
AND trade_history.selling=0                 
 order by alt_coin_id, id desc;
'''
cursor = conn.execute(sqlstr)
for row in cursor:
  dt = row[9].split(".")
  created_date = datetime.strptime(dt[0], '%Y-%m-%d %H:%M:%S')
  d=f'{created_date.day:02d}'+"/"+f'{created_date.month:02d}'+"/"+str(created_date.year)
  t=f'{created_date.hour:02d}'+":"+f'{created_date.minute:02d}'+":"+f'{created_date.second:02d}'
  print (row[1],row[6],d,t)
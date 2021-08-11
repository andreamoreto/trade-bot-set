import re

with open('./../binance-trade-bot/ratios.txt', 'r') as file:
    f=file.read()
f=f.replace(",","\n").replace("{","\n").replace("}","\n").replace(" <","").replace("<","")
f=re.sub(':{2}.*:','',f)   
print (f) 

#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import json
import requests

#Local imports
from stock import Stock
import mylogging as mylog

__KEYFILE__ = '.alpacakeys.txt'

def getKeys():
  keyfile = open(__KEYFILE__, 'r')
  keys = json.load(keyfile)
  coreurl = keys['paper']
  au = {'accUrl': "{}/v2/account".format(coreurl)}
  ou = {'orderUrl': '{}/v2/orders'.format(coreurl)}
  keys.update(au)
  keys.update(ou)
  print(keys)
  keyfile.close()
  return keys


def connect():
  keys = getKeys()
  headers = {'APCA-API-KEY-ID': keys['APIkeyID'],'APCA-API-SECRET-KEY': keys['secretkey']}
  r = requests.get(keys['accUrl'], headers = headers)
  return json.loads(r.content)

def buy(inStock):
  mylog.baseLog("Buy {n}, Last: {l}, MA: {ma}"
      .format(n=inStock.getName(), l=inStock.getLast(), ma=inStock.getMA()))
  print("Buy at {l}".format(l=inStock.getLast()))
  return 1

def sell(inStock):
  mylog.baseLog("Sell {n}, Last: {l}, MA: {ma}"
      .format(n=inStock.getName(), l=inStock.getLast(), ma=inStock.getMA()))
  print("Sell at {l}".format(l=inStock.getLast()))
  return 0
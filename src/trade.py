#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import json

#Local imports
from stock import Stock
import mylogging as mylog

__KEYFILE__ = '.alpacakeys.txt'

def connect():
  keyfile = open(__KEYFILE__, 'r')
  keys = json.load(keys)
  print(keys)
  keyfile.close()
  return

def buy(inStock):
  mylog.baseLog("Buy {n}, Last: {l}, MA: {ma}"
      .format(n=inStock.getName(), l=inStock.getLast(), ma=inStock.getMA()))
  return 1

def sell(inStock):
  mylog.baseLog("Sell {n}, Last: {l}, MA: {ma}"
      .format(n=inStock.getName(), l=inStock.getLast(), ma=inStock.getMA()))
  return 0
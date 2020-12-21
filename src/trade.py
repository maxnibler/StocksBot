#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys

#Local imports
from stock import Stock
import mylogging as mylog

def buy(inStock):
  mylog.baseLog("Buy {n}".format(n=inStock.getName()))
  return

def sell(inStock):
  mylog.baseLog("Sell {n}".format(n=inStock.getName()))
  return
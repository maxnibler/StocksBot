#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import yfinance as yf
import json
from datetime import datetime

#Local imports
from stock import Stock 
from dump import Dump
import mylogging as mylog
import trade

__DUMP__ = 'testDump.txt'
__DURATION__= 40
__CLOSE__ = datetime.strptime('15:59:00', '%H:%M:%S').time()

def checkStock(inStock):
  ma = inStock.getMA(__DURATION__)
  last = inStock.getLast()
  if ma >= last:
    if inStock.getHolding() == -1:
      return 0
    elif isStock.getHolding() == 0: 
      return 1
    elif isStock.getHolding() > 0:
      return 0
  else:
    if inStock.getHolding() == -1:
      inStock.updateHolding(0)
      return 0
    elif isStock.getHolding() == 0: 
      return 0
    elif isStock.getHolding() > 0:
      return -1

def main():
  data = Dump(__DUMP__)
  stockData = data.getStocks()
  myStocks = []
  for sd in stockData:
    newStock = Stock(sd['name'], sd['holding'])
    myStocks.append(newStock)

  toJson = []
  for stock in myStocks:
    toJson.append(stock.dump())

  while __CLOSE__ != myStocks[0].getTime():
    for stock in myStocks:
      indicator = checkStock(stock)
      if indicator > 0:
        trade.buy(stock)
      elif indicator < 0:
        trade.sell(stock)

  print(toJson)
  data.outDump({'stocks':toJson})

if __name__ == '__main__':
  main()
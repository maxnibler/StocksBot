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
  if ma > last:
    if inStock.getHolding() == -1:
      inStock.updateHolding(0)
      return 0
    elif inStock.getHolding() == 0: 
      return 0
    elif inStock.getHolding() > 0:
      return -1
  else:
    if inStock.getHolding() == -1:
      return 0
    elif inStock.getHolding() == 0: 
      return 1
    elif inStock.getHolding() > 0:
      return 0

def main():
  data = Dump(__DUMP__)
  stockData = data.getStocks()
  myStocks = []
  for sd in stockData:
    newStock = Stock(sd['name'], sd['holding'])
    myStocks.append(newStock)

  print(trade.connect())

  if __CLOSE__ == myStocks[0].getTime():
    print('Market is closed')
    return

  mylog.baseLog('Open for the day')

  while __CLOSE__ != myStocks[0].getTime():
    for stock in myStocks:
      stock.update()
      indicator = checkStock(stock)
      if indicator > 0:
        stock.updateHolding(trade.buy(stock))
      elif indicator < 0:
        stock.updateHolding(trade.sell(stock))

  toJson = []
  for stock in myStocks:
    mylog.baseLog('{n} closed at {v}'.format(n=stock.getName(), v=stock.getLast()))
    toJson.append(stock.dump())
  print(toJson)
  data.outDump({'stocks':toJson})

if __name__ == '__main__':
  main()
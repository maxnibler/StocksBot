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

__DUMP__ = 'testDump.txt'
__DURATION__= 40
__CLOSE__ = datetime.strptime('15:59:00', '%H:%M:%S').time()

def checkStock(inStock):
  ma = inStock.getMA(__DURATION__)
  last = inStock.getLast()
  if ma > last:
    return 1
  return 0

def main():
  data = Dump(__DUMP__)
  stockData = data.getStocks()
  myStocks = []
  for sd in stockData:
    newStock = Stock(sd['name'], sd['holding'])
    myStocks.append(newStock)

  toJson = []
  for stock in myStocks:
    print(checkStock(stock))
    toJson.append(stock.dump())

  if __CLOSE__ == myStocks[0].getTime():
    print(toJson)
    data.outDump({'stocks':toJson})

if __name__ == '__main__':
  main()
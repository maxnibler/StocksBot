#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import yfinance as yf
import json

#Local imports
from stock import Stock 
from dump import Dump

__DUMP__ = 'testDump.txt'

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

  print(toJson)
  data.outDump({'stocks':toJson})

if __name__ == '__main__':
  main()
#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import yfinance as yf
import json

#Local imports
from stock import Stock 

DUMP = 'testDump.txt'

def readDump(filename):
  dumpFile = open('../db/'+filename, 'r')
  rd = json.load(dumpFile)
  dumpFile.close()
  return rd

def dumpJson(filename, jsonlist):
  dumpFile = open('../db/'+filename, 'w')
  json.dump(jsonlist, dumpFile)
  dumpFile.close()

stockNames = ['MSFT', 'COTY']
myStocks = []
for name in stockNames:
  newStock = Stock(name, 0)
  myStocks.append(newStock)

toJson = []
for stock in myStocks:
  print(stock.getMA(40), stock.getLast(), stock.dump())
  toJson.append(stock.dump())

dumpJson(DUMP, toJson)
print(readDump(DUMP))

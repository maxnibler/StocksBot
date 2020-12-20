#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import yfinance as yf
import json

#Local imports
from stock import Stock 

def readDump(filename):
  dumpFile = open('../db/'+filename, 'r')
  return json.load(dumpFile)

def dumpJson():
  dumpFile = open('../db/fakeFile.txt', 'w')
  json.dump({"This": "is", "A": "Test"}, dumpFile)

msftStock = Stock('MSFT', 0)
print(msftStock.getMA(40), msftStock.getLast(), msftStock.dump())
#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import yfinance as yf

#Local imports
from stock import Stock 

def printWorld():
  return ("Hello World!")

msftStock = Stock('MSFT', 0)
print(msftStock.getMA(40), msftStock.getLast(), msftStock.dump())
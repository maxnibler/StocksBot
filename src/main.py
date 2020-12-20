#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

import sys
import yfinance as yf
import numpy as np

print(sys.path)

def printWorld():
  return ("Hello World!")

msft = yf.Ticker('MSFT')
history = msft.history(interval='1m', period='1d')

def average(hl):
  if len(hl) == 1:
    return hl[0]
  else:
    save = hl.pop()
    ave = average(hl)
    ave += save
    ave /= 2
    return ave

class Stock:
  def __init__(self, name, holding):
    self.name = name
    self.holding = holding
    self.history = self.update()
  
  def update(self):
    ticker = yf.Ticker(self.name)
    return ticker.history(interval='1m', period='1d')

  def getMA(self, duration):
    highLow = []
    for i in range(1, duration+1):
      total = self.history['High'][-i] + self.history['Low'][-i]
      highLow.append(total/2)
    return average(highLow)

  def getLast(self):
    last = self.history['Close'][-1]
    return last


msftStock = Stock('MSFT', 0)
print(msftStock.getMA(40), msftStock.getLast())
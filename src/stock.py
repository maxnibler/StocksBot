#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import yfinance as yf
import json

def average(hl):
  total = 0
  for item in hl:
    total += item
  return total/len(hl)

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

  def updateHolding(self, amount):
    self.holding = amount
    return

  def getHolding(self):
    return self.holding

  def dump(self):
    myjson = {
      'name': self.name,
      'holding': self.holding,
    }
    return json.dumps(myjson)

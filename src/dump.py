#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
import json

def readDump(filename):
  dumpFile = open('../db/'+filename, 'r')
  rd = json.load(dumpFile)
  dumpFile.close()
  return rd

def dumpJson(filename, jsonlist):
  dumpFile = open('../db/'+filename, 'w')
  json.dump(jsonlist, dumpFile)
  dumpFile.close()

class Dump:
  def __init__(self, filename):
    self.filename = filename
    self.inJson = readDump(filename)

  def outDump(self, jsonList):
    dumpJson(self.filename, jsonList)

  def getStocks(self):
    return self.inJson['stocks']

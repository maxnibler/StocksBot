#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Package Imports
import sys
sys.path.append('/home/max/gitrep/StockBot/src')

#Local Imports
import stock
from test import MyTest

tests = []

def gen():
  firstTest = MyTest('Average', stock.average)
  firstTest.expect([5,13,14,16], 12)
  tests.append(firstTest)

def run():
  total = 0
  passed = 0
  for test in tests:
    total += 1
    if test.exec():
      passed += 1
  print('Main Tests, {p}/{t}'.format(p=passed, t=total))
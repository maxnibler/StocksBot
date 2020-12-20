#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Package Imports
import sys
sys.path.append('/home/max/gitrep/StockBot/src')

#Local Imports
import main

class MyTest:
  def __init__(self, title, function):
    self.title = title
    self.function = function

  def expect(self, args, expected):
    self.args = args
    self.expected = expected

  def exec(self):
    if (self.args == None):
      output = self.function()
    else:
      output = self.function(self.args)
    result = (output == self.expected)
    if (result):
      print('{t} Test: Success'.format(t=self.title))
    else:
      print('{t} Test: Failed'.format(t=self.title))
      print('Expected: {e} \nGot: {o}'.format(e=self.expected, o=output))
    return result

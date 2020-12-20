#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Lib imports
import sys
from datetime import datetime

__PATH__ = '../db/'
__FILE__ = 'logfile.txt'

def timeStamp():
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return now

def baseLog(msg):
  file = open(__PATH__+__FILE__, 'a')
  print(timeStamp())
  file.write(timeStamp()+': ')
  file.write(msg)
  file.write('\n')
  file.close()
  return

#Maximillian H Nibler
#max.nibler@gmail.com
#https://github.com/maxnibler/

#Package Imports
import sys

#Local Imports
import maintests
import stocktests

print('Main Tests:')
maintests.gen()
maintests.run()
print('\nStock Tests:')
stocktests.gen()
stocktests.run()
####################
# File description #
####################

#Creator: Jon Simonsen
#Version 1.0
#Last official change: 22.01.20

#Contains code to test that the Unidcounter class and its file reading function
#works as expected.

from unitcounter import UnitCounter
from unitcounter import readCounters

UNITS = ['bananas', 'breads', 'chocolate chip cookies', 'eggs', 'fishes', 'milk bottles', 'potatoes', 'abcdefghijklmnopqrstuvwxyz1234567890']
QUANTITIES = [19, 2, 8.0, 36, 5, -1, 9999, 13579]
FILENAME = 'out_test.txt'

counters = []
counters.append(UnitCounter(UNITS[0], QUANTITIES[0]))
for unit, num in zip(UNITS[1:-1],QUANTITIES[1:-1]):
    counters.append(UnitCounter(unit, num))

counters.append(UnitCounter(UNITS[-1]))

for counter in counters:
    counter.printCounter()

print('')   #Add newline
counters[-1].addToCount(QUANTITIES[-1])
counters[-1].setInfo('You robbed a lot of #@!.')
counters[-2].addToCount(-9876)
counters[-2].setInfo('Some potatoes were consumed.')
counters[0].setCount(0)
counters[0].setInfo('The bananas were stolen :(')
counters[2].setCount(-1.0)
counters[2].addToCount(8.0)

print(counters[0].getName() + '   ' + str(counters[0].getCount()) + '   ' + counters[0].getInfo() + '\n')

file = open(FILENAME, 'w')
for counter in counters:
    counter.printCounter(extended=True)
    counter.writeToFile(file)

file.close()
file = open(FILENAME, 'r')
counterList = readCounters(file)

for counter in counterList:
    counter.printCounter(extended=True)

file.close()

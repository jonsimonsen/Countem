from unitcounter import UnitCounter

UNITS = ["bananas", "breads", "chocolate chip cookies", "eggs", "fishes", "milk bottles", "potatoes", "abcdefghijklmnopqrstuvwxyz1234567890"]
QUANTITIES = [19, 2, 8, 36, 5, -1, 999999, 123456789]

counters = []
counters.append(UnitCounter(UNITS[0], QUANTITIES[0]))
for index in range(1, len(UNITS) - 1):
    counters.append(UnitCounter(UNITS[index], QUANTITIES[index]))

counters.append(UnitCounter(UNITS[-1]))

for counter in counters:
    counter.printCount()

print('')   #Add newline
counters[-1].addToCount(123456789)
counters[-2].addToCount(-987654)
counters[0].setCount(0)

for counter in counters:
    counter.printCount()

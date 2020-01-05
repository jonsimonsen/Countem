from unitcounter import UnitCounter

UNITS = ["bananas", "breads", "chocolate chip cookies", "eggs", "fishes", "milk bottles", "potatoes", "abcdefghijklmnopqrstuvwxyz1234567890"]
QUANTITIES = [19, 2, 8, 36, 5, -1, 9999, 13579]

counters = []
counters.append(UnitCounter(UNITS[0], QUANTITIES[0]))
for index in range(1, len(UNITS) - 1):
    counters.append(UnitCounter(UNITS[index], QUANTITIES[index]))

counters.append(UnitCounter(UNITS[-1]))

for counter in counters:
    counter.printCounter()

print('')   #Add newline
counters[-1].addToCount(QUANTITIES[-1])
counters[-1].setInfo("You robbed a lot of #@!.")
counters[-2].addToCount(-9876)
counters[-2].setInfo("Some potatoes were consumed.")
counters[0].setCount(0)
counters[0].setInfo("The bananas were stolen :(")

print(counters[0].getName() + '   ' + str(counters[0].getCount()) + '   ' + counters[0].getInfo())
print('')   #Add newline

for counter in counters:
    counter.printCounter(True)

NAME_LEN = 32   #Max Number of characters in UnitCounter's name
COUNT_LEN = 8   #Max Number of digits in UnitCounter's count
SEP1 = ': '         #Used between name and count in UnitCounter's repr and str methods.
SEP2 = '   - ' #Used between count and info in UnitCounter's repr method.

class UnitCounter(object):
    """A class for counting objects of a certain type"""

    def __init__(self, description, value = 0):
        """Create a counter with the given description and starting value.

        description should be a string with at most NAME_LEN characters.
        No setter will be made for _name, so make sure it's correct from the start.
        value in the constructor and the setters should be integers, but this will not be verified by the class.
        """

        if len(description) > NAME_LEN:
            self._name = description[0:NAME_LEN]
            print("Unitcounter description was shortened.\n")
        else:
            self._name = description

        if isinstance(value, int):
            self._count = value
        else:
            print('The counter requires an integer as its value. It will be initialized to zero.\n')
            self._count = 0
        self._info = ""

    def __repr__(self):
        """Return a string representing this counter."""

        return '{:{x}}'.format(self._name, x=NAME_LEN) + SEP1 + '{:>{y}}'.format(self._count, y=COUNT_LEN) + SEP2 + self._info

    def __str__(self):
        """Returns a string representing this counter. Unlike repr, it ignores info."""

        return '{:{x}}'.format(self._name, x=NAME_LEN) + SEP1 + '{:>{y}}'.format(self._count, y=COUNT_LEN)

    def getCount(self):
        """Getter for _count"""
        return self._count

    def setCount(self, value):
        """Setter for _count"""
        if isinstance(value, int):
            self._count = value
        else:
            print('The count must be set to an integer value. It will remain unchanged for now.\n')

    def addToCount(self, increment):
        """Increase count by the given increment. Increment can be negative"""
        if isinstance(increment, int):
            self._count += increment
        else:
            print('Additions to the count must be integers. Nothing will be added for now.\n')

    def getName(self):
        """Getter for _name"""
        return self._name

    def getInfo(self):
        """Getter for _info"""
        return self._info

    def setInfo(self, info):
        """Setter for _info"""
        self._info = info

    def makeCopy(self):
        """Return a copy of the counter (having the same values for all attributes)"""
        counter = UnitCounter(self._name, self._count)
        counter.setInfo(self._info)
        return counter

    def printCounter(self, extended = True):
        """Print the name and value of the counter. Also print info if extended is True."""

        if extended:
            print(repr(self))
        else:
            print(str(self))

    def writeToFile(self, handle):
        """Write the representation of this counter to the file connected to handle. Assumes that the file is in 'w' or 'a' mode."""
        handle.write(repr(self) + '\n')

def readCounters(handle):
    """Read all Unitcounters from the file that handle handles and return a list of these counters."""

    #Initialize variables
    result = []
    newCounter = None
    name = ''
    count = 0
    counters = handle.readlines()

    #Parse the read lines and make new counters.
    for c in counters:
        name = c[:NAME_LEN]
        count = int(c[NAME_LEN + len(SEP1):NAME_LEN + COUNT_LEN + len(SEP1)])
        newCounter = UnitCounter(name, count)
        if len(c) > NAME_LEN + COUNT_LEN + len(SEP1) + len(SEP2):
            newCounter.setInfo(c[NAME_LEN + COUNT_LEN + len(SEP1) + len(SEP2):-1]) #ignore newline
        #Add the counter to the result list
        result.append(newCounter)

    return result

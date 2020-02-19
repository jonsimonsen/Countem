####################
# File description #
####################

#Creator: Jon Simonsen
#Version 1.0+
#Last official change: 19.02.20

#Contains a class for UnitCounters, a function for reading these from a file
#and some class-specific global constants.

#Imports
from manager.saveable import Saveable

#Class definition
class UnitCounter(Saveable):
    """A class for counting objects of a certain type"""

    #Class level attributes
    _nameLen = 32   #Max Number of characters in UnitCounter's name
    _countLen = 8   #Max Number of digits in UnitCounter's count
    _nameSep = ': ' #Used between name and count in UnitCounter's repr and str methods.

    def __init__(self, description, value = 0):
        """Create a counter with the given description and starting value.

        description should be a string with at most _nameLen characters.
        No setter will be made for _name, so make sure it's correct from the start.
        value in the constructor and the setters should be integers.
        """

        #Initialize info to the empty string as requested by the parent class.
        self._info = ''

        #Set name equal to the (valid part of the) description
        if len(description) > self._nameLen:
            self._name = description[0:self._nameLen]
            print('Unitcounter description was shortened.\n')
        else:
            self._name = description

        #Initialize count to equal value if a valid value is given
        if isinstance(value, int):
            self._count = value
        else:
            print('The counter requires an integer as its value. It will be initialized to zero.\n')
            self._count = 0

    def __str__(self):
        """Returns a string representing this counter."""

        return '{:{x}}'.format(self._name, x=self._nameLen) + self._nameSep + '{:>{y}}'.format(self._count, y=self._countLen)

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

    def makeCopy(self):
        """Return a copy of the counter (having the same values for all attributes)"""
        counter = UnitCounter(self._name, self._count)
        counter.setInfo(self._info)
        return counter

#Function that creates counter instances from a file
def readCounters(handle):
    """Read all Unitcounters from the file that handle references and return a list of these counters."""

    #Initialize variables
    result = []
    newCounter = None
    name = ''
    count = 0
    counters = handle.readlines()

    #Parse the read lines and make new counters.
    for c in counters:
        name = c[:UnitCounter._nameLen]
        count = int(c[UnitCounter._nameLen + len(UnitCounter._nameSep):UnitCounter._nameLen + UnitCounter._countLen + len(UnitCounter._nameSep)])
        newCounter = UnitCounter(name, count)
        if len(c) > UnitCounter._nameLen + UnitCounter._countLen + len(UnitCounter._nameSep) + len(UnitCounter._reprSep):
            newCounter.setInfo(c[UnitCounter._nameLen + UnitCounter._countLen + len(UnitCounter._nameSep) + len(UnitCounter._reprSep):-1]) #ignore newline
        #Add the counter to the result list
        result.append(newCounter)

    return result

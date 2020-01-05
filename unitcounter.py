NAME_LEN = 32

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

        self._count = value
        self._info = ""

    def __repr__(self):
        """Return a string representing this counter."""

        return '{:32}: '.format(self._name) + '{:>8}   - '.format(self._count) + self._info

    def __str__(self):
        """Returns a string representing this counter. Unlike repr, it ignores info."""

        return '{:32}: '.format(self._name) + '{:>8}'.format(self._count)

    def getCount(self):
        """Getter for _count"""
        return self._count

    def setCount(self, value):
        """Setter for _count"""
        self._count = value

    def addToCount(self, increment):
        """Increase count by the given increment. Increment can be negative"""
        self._count += increment

    def getName(self):
        """Getter for _name"""
        return self._name

    def getInfo(self):
        """Getter for _info"""
        return self._info

    def setInfo(self, info):
        """Setter for _info"""
        self._info = info

    def printCounter(self, extended = False):
        """Print the name and value of the counter. Also print info if extended is True."""

        if extended:
            print(repr(self))
        else:
            print(str(self))

    def writeToFile(self, handle):
        """Write the representation of this counter to the file connected to handle. Assumes that the file is in 'w' or 'a' mode."""
        handle.write(repr(self) + '\n')
        

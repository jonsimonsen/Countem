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

    def getCount(self):
        """Getter for _count"""
        return self._count

    def setCount(self, value):
        """Setter for _count"""
        self._count = value

    def addToCount(self, increment):
        """Increase count by the given increment. Increment can be negative"""
        self._count += value

    def getName(self):
        """Getter for _name"""
        return self._name

    def getInfo(self):
        """Getter for _info"""
        return self._info

    def setInfo(self, info):
        """Setter for _info"""
        self._info = info

    def printCount(self, extended = False):
        """Print the name and value of the counter. Also print info if extended is True."""

        prefix = self._name
        prefix += " " * (NAME_LEN - len(self._name))
        print(prefix + ": " + str(self._count))
        #Printing info is not implemented yet. Should look into right-adjusting the count first.
        

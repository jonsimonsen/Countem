####################
# File description #
####################

#Creator: Jon Simonsen
#Version 1.1
#Last official change: 19.02.20

#Contains a menu-driven environment for managing UnitCounters.
#This includes adding, modifying, displaying, saving and loading instances.

#Imports
from unitcounter import UnitCounter, readCounters
from manager.manager import Manager
from manager.user_io import getPosInt, clearTerminal
import os

class CountManager(Manager):
    """A class for managing counts (UnitCount objects)."""
    _fileName = 'count_out.txt'
    _greeting = '\nWelcome to Countem, an app for managing counts of things.\n\n'
    _info = "The app will use the file '" + _fileName + "' in this directory for loading and saving data.\n"

    def addObject(self):
        """Class specific helper for the add method that does the actual creation of a new unitcounter object.

        Prompts the user for input to create a new counter.

        Returns the counter.
        """
        #Ask for the name of the counter
        prompt = 'Please enter the name of the counter (Max. ' + str(UnitCounter._nameLen) + ' characters): '
        name = input(prompt)
        while len(name) == 0 or len(name) > UnitCounter._nameLen:
            name = input('The name must be between 1 and ' + str(UnitCounter._nameLen) + ' characters long. Try again: ')

        #Ask for the count
        clearTerminal()
        count = getPosInt('The count', 10**UnitCounter._countLen - 1)

        #Create the counter
        return UnitCounter(name, int(count))

    def changeObject(self, index):
        """Function for creating a new counter based on an existing one and returning the new one along with a reference to the old one.
        counterList is a list of UnitCounters.
        The function prompts the user for what counter is to be replaced and then how to change it.
        Clears the terminal before returning.
        Returns a tuple consisting of the new counter and the index of the one to be replaced.
        The new counter will be returned as None if the user chose to delete a counter.
        Returns None if the user decided to not change anything after all. Also prints some status info after clearing the terminal when returning None.
        """

        counter = self._collection[index].makeCopy()
        print('Choose a new value for the count.\n')
        count = getPosInt('The count', 10**UnitCounter._countLen - 1)
        counter.setCount(count)
        return (counter, index)

    def readObjects(self, file):
        """Use the class specific read function to create counters based on reading them from file.

        file should be a handle to the file where counters are stored.
        """

        self._collection = readCounters(file)

##########################
# Main (executable code) #
##########################

app = CountManager('Count', 'Counts')
app.run()

# Countem
UnitCounter is a utility class for counts of objects with a description and an option to add information. Countem is an application for managing such counters.

# Usage
-To use the menu-driven counter management application, run the command python3 countem.py from a terminal in the cloned repo.  
-A default path for loading and saving counters exists. To make sure that a counter list (file) is safe, it is suggested that lists that you want to keep are copied or moved to other locations (probably a good idea to give them a descriptive name instead of the default one too). If they need to be accessed later, it is suggested that a copy is put back in the repo and given the default name, or that the default name is changed (but make sure that this does not run the risk of overwriting important files).  
-How to use the utility class will not be explained in detail. I will assume that anyone that uses its filewriting function makes sure that important information is not lost in the process.  
-A test file can be run with the command python3 test_counts.py after forking this repo. Be aware that the test file will create or overwrite existing files with the name 'out_test.txt' (or some other name if the filename is manually changed in the test file) in that repo.  

# Testing
-Some basic tests have been run to confirm that the class and the menu-driven app works as expected.  
-Because everything hasn't been thoroughly tested it is suggested that a clone of the project is kept in its own repo and that executable code is run from there, that changes to paths does not access file space outside that repo and that generated files are backed up in a reasonable place (preferrably outside the repo) so they can be retrieved later if the content gets messed up.  
-The development has been done in a Linux environment, but the code should work from a Windows command window too. This will probably be tested soon.

# History

# Version 1 (complete description):
-unitcounter.py contains a class for counting units ranging from 0 to 99999999 (the highest number that can be displayed with COUNT_LEN digits).  
-Each counter has a name that must be between 1 and 32 (NAME_LEN) characters.  
-A new counter has no additional info, but this can be added using setInfo().  
-Every attribute except name can be set after creation. It is the callee's task to ensure that the count stays within the excepted range, but it does handle non-integer arguments by giving a message and doing nothing more.  
-__repr__ is used to create a representation of the counter that is used for loading from and saving to files. It is also used for conditionally printing all attributes.  
-__str__ is used for printing attributes that does not include info.  
-unitcounter.py also contains a standalone method that reads counters from a file and returns a list with all of them.  

-countem.py contains methods and runnable code for creating, modifying and storing UnitCounters.  
-It runs in terminal and is menu-driven.  
-It allows loading, viewing, creating, modifying and saving counters. Deletion is considered as modifying.  
-Navigating the list of counters when displaying or choosing what counter to modify is done by constructing pages and prompting the user in a stepwise operation.  
-It enforces the constraints that the UnitCounter class puts on the attributes of the counters (also when calling setters).  
-There is no rule for uniqueness and counters are kept in the order they are created.  

-test_counts.py contains some basic tests of the counter class.  
-a different file has been made to test a few of the possible cases for input to countem.py. It will not be published in the repo.  

# Temporary version 0.155:
-Can save all counters to file.  
-Can modify a counter.  
-Can clear the terminal to make the output look better.  
-The UnitCounter class has a method to copy a counter by making a new one with the same values.  
-Counters can be displayed stepwise. Need to test with differently sized counter lists.

# Version 0.15:
-The function readCounters() parses a file that contains counters into a list of counter objects.  
-If non-integers are being used to try to mutate the count, nothing is changed and a corresponding message is displayed.  
-The file countem.py has been added for managing counters in a menu-driven environment from terminal/command prompt.  
-It can read from file, display all counters and add new counters.

# Version 0.1:
-The class has proper init, repr and str methods. It has getters and setters for name, count and info except that name can't be set outside init. The name will not be longer than 32 characters. The count will not be correctly represented if it's higher than 99999999.  
-The class has methods for printing a representation of itself and for writing a represenation of itself to an open file.  
-There is a test file to check that most functionality works satisfactorily.  

# Pre-versions:
-Made a class without the ability to print info directly. Made a test file to verify that the class works as expected.  

# Ideas for additional functionality
-Consider preventing loading and saving when nothing has been altered since the last load. Saving can be handled by using the value of modified, and loading can probably be handled by combining len(counters) and modified.  
-Make a graphical user interface. This is not considered a priority, but it would prevent prompting the user twice about deleting a counter.  
-Enable loading that does not overwrite the current list of counters. This is especially useful if combining multiple files is desireable.  
-Change the repo name to Countem since focus has moved from the counter class itself to the counter management application.  

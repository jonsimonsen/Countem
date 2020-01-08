# UnitCounter
A utility class for counts of objects with a description and an option to add information.

# Usage
How to use the utility class will not be explained in detail. I will assume that anyone that uses its filewriting function makes sure that important information is not lost in the process.  
A test file can be run with the command python3 countertest.py after forking this repo. Be aware that the test file will create or overwrite existing files with the name 'output.txt' (or some other name if the filename is manually changed in the test file) in that repo.  

# History
Pre-versions: Made a class without the ability to print info directly. Made a test file to verify that the class works as expected.  

# Version 0.1:
-The class has proper init, repr and str methods. It has getters and setters for name, count and info except that name can't be set outside init. The name will not be longer than 32 characters. The count will not be correctly represented if it's higher than 99999999.  
-The class has methods for printing a representation of itself and for writing a represenation of itself to an open file.  
-There are no tests to handle incorrect parameters to the class methods.  
-There is a test file to check that most functionality works satisfactorily.  

# Current version:
-The function readCounters() parses a file that contains counters into a list of counter objects.

# TODO
Make code that uses the UnitCounter class.  

# UnitCounter
Planning to make a utility class for counts of objects with a description and probably an option to add information.

# History
Pre-versions: Made a class without the ability to print info directly. Made a test file to verify that the class works as expected.
Version 0.1: The class has proper init, repr and str methods. It has getters and setters for name, count and info except that name can't be set outside init. The name will not be longer than 32 characters. The count will not be correctly represented if it's higher than 99999999.
-The class has methods for printing a representing of itself and for writing a represenation of itself to an open file.
-There are no tests to handle incorrect parameters to the class methods.
-There is a test file to check that most functionality works satisfactorily.
-TODO: Clean up the README file and make a function for reading counters from a file.

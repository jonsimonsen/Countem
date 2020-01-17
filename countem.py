from unitcounter import UnitCounter, readCounters, NAME_LEN, COUNT_LEN
import os

FILENAME = 'count_out.txt'
GREETING = "\nWelcome to Countem, an app for counting things.\n\n"
INFO = "This app will use the file '" + FILENAME + "' in this directory for loading and saving data.\n"
PAGESIZE = 16   #Number of counters to display on a page (when modifying)

def clearTerminal():
    """Clear the terminal or command window that python is running in. Found at
    https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def makeMenu():
    """Makes a menu displaying the options the user can choose from."""
    header = "Please choose what to do next:\n"
    sep    = "------------------------------\n"
    op1 = "1: Load counters from file\n"
    op2 = "2: Display all counters\n"
    op3 = "3: Add a new counter\n"
    op4 = "4: Modify an existing counter\n"
    op5 = "5: Save all counters\n"
    op6 = "6: Exit\n"

    print(header + sep + op1 + op2 + op3 + op4 + op5 + op6)

def getConfirmation():
    """Prompts the user for input until 'y' or 'n' has been entered.
    An explanation of what the user can confirm should be given before calling the function.
    Returns True if 'y' and False if 'n'"""
    answer = ''

    while answer not in ['y', 'n']:
        answer = input("Press 'y' for yes or 'n' for no and hit enter: ")

    if answer == 'y':
        return True
    else:
        return False

def getPosInt(valName, maxVal):
    """Prompt the user for an integer until a non-negative integer that is not higher than maxVal is entered. Returns that integer."""
    #Initial prompt
    prompt = "Enter " + valName.lower() + " (Max. " + str(maxVal) + "): "
    num = -1
    while True:
        count = input(prompt)
        #Try to convert to an int. Change the prompt for the next iteration (if any)
        try:
            num = int(count)
            if num < 0:
                prompt = valName + ' must be a positive integer or zero. Try again: '
            elif num > maxVal:
                prompt = valName + ' must be ' + str(maxVal) + ' or less. Try again: '
            else:
                break
        except ValueError:
            prompt = valName + ' must be an integer. Try again: '
    return num

def addCounter():
    """Prompts the user for input to create a new counter and asks if it should be added.
    returns the counter if the user says yes and None otherwise."""
    #Ask for the name of the counter
    prompt = "Please enter the name of the counter (Max. " + str(NAME_LEN) + " characters): "
    name = input(prompt)
    while len(name) == 0 or len(name) > NAME_LEN:
        name = input("The name must be between 1 and " + str(NAME_LEN) + " characters long. Try again: ")

    #Ask for the count
    count = getPosInt("The count", 10**COUNT_LEN - 1)

    #Create the counter
    counter = UnitCounter(name, int(count))

    #Add info if the user wishes
    info = input("Type any additional info and press enter (press enter directly if there is no additional info): ")
    if len(info):
        counter.setInfo(info)

    #Display the counter and ask if it should be added
    print ('')  #Add newline for readability
    print("Here is your counter:\n")
    counter.printCounter()
    print ('')  #Add newline for readability
    print("Do you want to add it to your list of counters?\n")
    answer = getConfirmation()

    if answer == True:
        return counter

    return None

def changeCounter(counterList):
    """Function for creating a new counter based on an existing one and returning the new one along with a reference to the old one.
    counterList is a list of UnitCounters.
    The function prompts the user for what counter is to be replaced and then how to change it.
    Returns a tuple consisting of the new counter and the index of the one to be replaced.
    Returns None if the user decided to not change anything after all.
    """
    #If no counters were provided, there's nothing to change
    if len(counterList) == 0:
        print("There are no counters to modify.\n")
        return None

    #Print information to the user
    print("You will now be presented with a list of the counters you can modify.\n"
    "Each will be preceded by its index.\n")
    input("Press enter to continue: ")

    max_index = len(counterList)
    choice = 'n'
    current = 0
    options = list(range(len(counterList)))
    options = [str(i) for i in options]
    options.append('q')
    options.append('n')

    #Loop through the list until the user chooses an index or to quit
    while choice == 'n':
        for i in range(1 + (len(counterList) - 1) // PAGESIZE):
            print('\nList of counters, page ' + str(i + 1) + ':\n')
            for j in range(PAGESIZE):
                current = PAGESIZE * i + j
                if current < len(counterList):
                    print(str(current) + ": ", end='')
                    counterList[current].printCounter()
                else:
                    break

            print("\nEnter the index of the counter to modify. Alternatively, enter 'n' to see the next page of counters or 'q' to get back to the main menu.\n")
            choice = ''
            while not choice in options:
                choice = input("Choice: ")

            if choice == 'n':
                continue
            else:
                break

    if choice == 'q':
        return None
    else:
        index = int(choice)
        counter = counterList[index].makeCopy()
        print("You can now modify the following counter:\n")
        counter.printCounter()
        print("Choose a new value for the count.\n")
        count = getPosInt("The count", 10**COUNT_LEN - 1)
        counter.setCount(count)
        info = input("Choose new value for into: ")
        counter.setInfo(info)

    return (counter, index)

#Runnable code

#Variable initialization
running = True
counters = []
file = None
prompt = ''
print(GREETING + INFO)
modified = False    #True if counters have been added since last load, false otherwise.
#loaded, modified, opened

clearTerminal()
while running:
    makeMenu()
    res = input("Enter the digit corresponding to your choice: ")
    print('')   #Make newline
    if res == "1":
        reading = True
        if modified:
            print("Loading from file will overwrite all current counters. Are you sure you want to do this?\n")
            reading = getConfirmation() #Do not proceed if the user doesn't confirm

        clearTerminal()
        if reading:
            file = open(FILENAME, "r")
            counters = readCounters(file)
            file.close()
            print("Data was read from file.\n")
            modified = False
        else:
            print("No data was read.\n")
    elif res == "2":
        clearTerminal()
        if len(counters) == 0:
            print("No counters have been added yet.")
        for c in counters:
            c.printCounter()
        print ('')  #Add newline for readability
    elif res == "3":
        counter = addCounter()
        if counter is not None:
            counters.append(counter)
            modified = True
        print ('')  #Add newline for readability
    elif res == "4":
        counterTup = changeCounter(counters)
        counter = counterTup[0]

        #Display the old and new counter and ask if it the changes are ok
        print ('')  #Add newline for readability
        print('The original counter was:\n')
        counters[counterTup[1]].printCounter()
        print("\nHere is your new counter:\n")
        counter.printCounter()
        print ('')  #Add newline for readability
        print("Do you want to keep these changes?\n")
        answer = getConfirmation()

        if answer == True:
            counters[counterTup[1]] = counter
            print("Counter updated.\n")
            modified = True
        else:
            print('Modification aborted.\n')
    elif res == "5":
        print("saving will overwrite all content in '" + FILENAME + "'. Are you sure?\n")
        if getConfirmation():
            file = open(FILENAME, "w")
            for counter in counters:
                counter.writeToFile(file)
            file.close()
            modified = False
            print("Data saved.\n")
        else:
            print("Save aborted.\n")
    elif res == "6":
        quitting = True
        if modified:
            print("You have made unsaved changes to the counters. Are you sure you want to exit without saving?\n")
            quitting = getConfirmation()
            print ('')  #Add newline for readability

        if quitting:
            running = False
            print("Have a nice day.\n")
    else:
        print("You entered an invalid option. Try again.\n")

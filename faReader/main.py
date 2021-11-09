from FiniteAutomata import *


def printMenu():
    print()
    print("FA Menu:" + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Display set of states")
    print("2. Display the set of final states")
    print("3. Display the alphabet")
    print("4. Display the transitions")
    print("5. Check if a sequence is accepted by the current FA")
    print("6. Check if sequences read from a file are accepted by the current FA")
    print("0. Exit menu")


if __name__ == '__main__':

    myFaReader = FiniteAutomata("fa.in")
    myFaReader.readFromFile()

    while True:
        printMenu()
        operation = int(input("Please enter a command:\n"))
        if operation == 0:
            break
        if operation == 1:
            print(myFaReader.getAllStatesString())
        if operation == 2:
            print(myFaReader.getFinalStatesString())
        if operation == 3:
            print(myFaReader.getAlphabetString())
        if operation == 4:
            print(myFaReader.getTransitionsString())
        if operation == 5:
            sequence = input("sequence = ")
            result = myFaReader.belongsToFa(0, sequence, myFaReader.getInitialStateString())
            result = "is accepted" if result is True else "is not accepted"
            print("The sequence " + str(sequence) + " " + result + " by the current FA")
        if operation == 6:
            filename = input("filename = ")
            faFile = open(filename, "r")
            lines = faFile.readlines()
            for line in lines:
                line = line.split()
                result = myFaReader.belongsToFa(0, line, myFaReader.getInitialStateString())
                result = "is accepted" if result is True else "is not accepted"
                print("The sequence " + str(line) + " " + result + " by the current FA")
        if operation not in range(0, 7):
            print("Inexistent command")





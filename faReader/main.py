from FiniteAutomata import *

if __name__ == '__main__':
    myFaReader = FiniteAutomata("fa.in")
    # 1: Reads the elements of a FA (from file)
    myFaReader.readFromFile()
    # 2: Displays the elements of a finite automata, using a menu:
    # the set of states, the alphabet, all the transitions, the set of final states.
    myFaReader.displayFaElements()
    # 3: For a DFA, verify if a sequence is accepted by the FA.
    faFile = open("sequences.txt", "r")
    lines = faFile.readlines()
    for line in lines:
        line = line.split()
        result = myFaReader.belongsToFa(0, line, myFaReader.getInitialStateString())
        result = "is accepted" if result is True else "is not accepted"
        print("The sequence " + str(line) + " " + result + " by the current FA")


class FiniteAutomata:
    def __init__(self, faFilename):
        self.__faFilename = faFilename
        self.__initialState = ""
        self.__finalStates = []
        self.__states = []
        self.__alphabet = []
        self.__transitions = {}


    def readFromFile(self):
        faFile = open(self.__faFilename, "r")
        lines = faFile.readlines()
        self.__initialState = lines[0].split()
        self.__initialState = self.__initialState[0]
        self.__finalStates = lines[1].split()
        self.__states.extend(self.__initialState)
        self.__states.extend(self.__finalStates)

        for line in lines[2:]:
            if line != "\n":
                fromNode, toNode, alphabetValue = line.split()
                if fromNode not in self.__states:
                    self.__states.append(fromNode)
                if toNode not in self.__states:
                    self.__states.append(toNode)
                if alphabetValue not in self.__alphabet:
                    self.__alphabet.append(alphabetValue)
                if fromNode not in self.__transitions.keys():
                    self.__transitions[fromNode] = [[toNode, alphabetValue]]
                else:
                    self.__transitions[fromNode].append([toNode, alphabetValue])


        faFile.close()

    def getInitialStateString(self):
        return self.__initialState


    def getFinalStatesString(self):
        fStatesString = ""
        for state in self.__finalStates:
            fStatesString += state + " "
        return fStatesString

    def getAllStatesString(self):
        allStatesString = ""
        for state in self.__states:
            allStatesString += state + " "
        return allStatesString


    def getTransitionsString(self):
        transitionsString = ""
        for fromState in self.__transitions.keys():
            transitionsString += "State " + fromState + ":\n"
            for toState in self.__transitions[fromState]:
                transitionsString += "     " + fromState + " -> " + toState[0] + ": " + toState[1] + "\n"
        return transitionsString


    def displayFaElements(self):
        print("Fa Elements")
        print("Initial state: " + self.getInitialStateString())
        if len(self.__finalStates) == 1:
            print("Final state: " + self.getFinalStatesString())
        else:
            print("Final states: " + self.getFinalStatesString())
        print("All states: " + self.getAllStatesString())
        print("Transitions:")
        print(self.getTransitionsString())


    def getPossibleTransitions(self, letter, currentState):
        transitions = []
        if currentState in self.__transitions.keys():
            for transition in self.__transitions[currentState]:
                if transition[1] == letter:
                    transitions.append(transition[0])
        return transitions


    def belongsToFa(self, position, sequence, currentState):
        if position < len(sequence):
            letter = sequence[position]
            possibleTransitions = self.getPossibleTransitions(letter, currentState)
            if len(possibleTransitions) == 0:
                return False

            for state in possibleTransitions:
                if state in self.__finalStates and position == len(sequence) - 1:
                    return True
                if self.belongsToFa(position + 1, sequence, state):
                    return True
        return False






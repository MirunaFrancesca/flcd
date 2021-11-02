class SymbolTable:
    def __init__(self, length, stFilename):
        self.__length = length
        self.__symtable = [[[] for i in range(1)] for j in range(length)]
        self.__stFilename = stFilename

    def dumpDataToFile(self):
        stFile = open(self.__stFilename, "w")
        toPrint = ""
        for key in range(len(self.__symtable)):
            toPrint += "Key" + str(key) + ": [ "
            for value in self.__symtable[key]:
                toPrint += str(value) + " "
            toPrint += "]\n"
        stFile.write(toPrint)
        stFile.close()

    def hashFunction(self, element):
        return hash(element) % self.__length

    def addToST(self, type, element):
        hashValue = self.hashFunction(element)
        for pos in range(len(self.__symtable[hashValue])):
            if len(self.__symtable[hashValue][pos]) == 2 and \
                    self.__symtable[hashValue][pos][1] == element:
                return [hashValue, pos]

        self.__symtable[hashValue].append([type, element])
        return [hashValue, len(self.__symtable[hashValue]) - 1]



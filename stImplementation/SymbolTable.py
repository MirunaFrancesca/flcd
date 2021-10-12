class SymbolTable:
    def __init__(self, length):
        self.__length = length
        self.__symtable = [[[] for i in range(1)] for j in range(length)]

    def hashFunction(self, element):
        return hash(element) % self.__length

    def addToST(self, type, element):
        hashValue = self.hashFunction(element)
        for pos in range(len(self.__symtable[hashValue])):
            if len(self.__symtable[hashValue][pos]) == 2 and \
                    self.__symtable[hashValue][pos][1] == element:
                return pos

        self.__symtable[hashValue].append([type, element])
        return len(self.__symtable[hashValue]) - 1



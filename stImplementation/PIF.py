class PIF:
    def __init__(self, pifFilename):
        self.__pifFilename = pifFilename
        self.__pifList = []

    def dumpDataToFile(self):
        pifFile = open(self.__pifFilename, "w")
        toPrint = ""
        for value in self.__pifList:
            toPrint = toPrint + str(value) + "\n"
        pifFile.write(toPrint)
        pifFile.close()

    def addToPIF(self, token, index):
        self.__pifList.append([token, index])
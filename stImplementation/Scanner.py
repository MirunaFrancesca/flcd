import re

class Scanner:
    def __init__(self, st, pif, srcFilename, tokensFilename):
        self.__st = st
        self.__pif = pif
        self.__lexicalCorrectness = ''
        self.__sourceFilename = srcFilename
        self.__tokensFilename = tokensFilename
        self.__tokens = self.readTokens()

    def readTokens(self):
        tokensFile = open(self.__tokensFilename, "r")
        content = tokensFile.read()
        tokensFile.close()
        return content.split(",")

    def isBoolean(selfself, token):
        return token in ["true", "false"]

    def isNumber(self, token):
        return re.match('^[-+]?[1-9]+[0-9]*$', token) is not None or token == "0"

    def isChar(self, token):
        return re.match('^["\'][a-zA-Z0-9~`!@#$%^&*"_]["\']$', token)

    def isString(self, token):
        return re.match('^["\'][_a-zA-Z0-9]+["\']$', token)

    def isIdentifier(self, token):
        return re.match('^[_a-zA-Z][_a-zA-Z0-9]*$', token)

    def identifyToken(self, token):
        if token in self.__tokens:
            return 'token'
        if self.isNumber(token) or self.isChar(token) or self.isString(token) or self.isBoolean(token):
            return 'constant'
        if self.isIdentifier(token):
            return 'identifier'
        return 'Lexical error'

    def scan(self):
        srcFile = open(self.__sourceFilename, "r")
        # lines = srcFile.readlines()
        content = srcFile.read().split()
        srcFile.close()

        for token in content:
            if len(token) > 1:
                if re.search('[:\.,]', token) is not None:
                    token1 = token[:len(token)-1]
                    token2 = token[len(token)-1:]
                    type = self.identifyToken(token1)
                    if type in ["constant", "identifier"]:
                        pos = self.__st.addToST(type, token1)
                        self.__pif.addToPIF(type, pos)
                        self.__pif.addToPIF(token2, -1)
                    else:
                        if type == "token":
                            self.__pif.addToPIF(token, -1)
                        else:
                            self.__lexicalCorrectness = "Lexical error at " + token1
                            return self.__lexicalCorrectness
                else:
                    type = self.identifyToken(token)
                    if type in ["constant", "identifier"]:
                        pos = self.__st.addToST(type, token)
                        self.__pif.addToPIF(type, pos)
                    else:
                        if type == "token":
                            self.__pif.addToPIF(token, -1)
                        else:
                            self.__lexicalCorrectness = "Lexical error at " + token
                            return self.__lexicalCorrectness
            else:
                type = self.identifyToken(token)
                if type in ["constant", "identifier"]:
                    pos = self.__st.addToST(type, token)
                    self.__pif.addToPIF(type, pos)
                else:
                    if type == "token":
                        self.__pif.addToPIF(token, -1)
                    else:
                        self.__lexicalCorrectness = "Lexical error at " + token
                        return self.__lexicalCorrectness

        self.__pif.dumpDataToFile()
        self.__st.dumpDataToFile()
        self.__lexicalCorrectness = "Lexically correct. \nCheck PIF and ST files for details."
        return self.__lexicalCorrectness







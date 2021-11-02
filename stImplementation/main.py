from PIF import PIF
from Scanner import Scanner
from SymbolTable import SymbolTable

if __name__ == '__main__':

    pifFilename = "PIF.out"
    myPif = PIF(pifFilename)
    stFilename = "ST.out"
    length = 29
    mySt = SymbolTable(length, stFilename)
    srcFilename = "p1.txt"
    tokensFilename = "tokens.in"
    myScanner = Scanner(mySt, myPif, srcFilename, tokensFilename)
    print(myScanner.scan())




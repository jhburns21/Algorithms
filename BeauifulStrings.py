import sys

filePath = sys.argv[1]

def main():
    with open(filePath, "r+") as inputFile:
        for scentence in inputFile:
            letters = list(scentence)
            letterDict = {}
            for l in letters:
                testLetter = ord(l.lower())
                if testLetter >= 97 and testLetter <= 122:
                    if letterDict.has_key(testLetter):
                        letterDict[testLetter] += 1
                    else:
                        letterDict[testLetter] = 1
            #letter Dict has all letters counted
            points = 26
            total = 0
            for val in enumerate(letterDict):
                maxNum = max(letterDict.iterkeys(), key=(lambda key: letterDict[key]))
                total = total + (letterDict[maxNum] * points)
                letterDict[maxNum] = 0
                points-=1
            print total
            total = 0


if __name__ == '__main__':
    main()

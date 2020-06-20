def CountWordsFromFile():
        fileName=input("enter the file name:-")
        nuberOfWords=0
        file=open(fileName,'r')
        for line in file:
                words=line.split()
                numberOfWords=numberOfWords+len(words)

        print("numberOfWords:")
        print( numberOfWords)

CountWordsFromFile()
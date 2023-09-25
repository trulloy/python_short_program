parentString = "hellohet helloamit hy"
subString = "hello"
flag = False

parentLength = len(parentString)
subStringLength = len(subString)
currentIndexSubString = 0 
countWords = 0
for i in range(0,parentLength):
    # print("Parant char - " + parentString[i] + " : " + subString[currentIndexSubString])
    if parentString[i] == subString[currentIndexSubString]:
        currentIndexSubString = currentIndexSubString + 1
        if currentIndexSubString == subStringLength:
            countWords = countWords + 1
            currentIndexSubString = 0
    else:
        currentIndexSubString = 0
        continue
    
print("WordsCount: " + str(countWords))
print("CountByFun: " + str(parentString.count(subString)))
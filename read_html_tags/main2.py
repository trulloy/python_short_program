parentString = "hellh htth"
subString = "he"


parentLength = len(parentString)
subStringLength = len(subString)
currentIndexSubString = 0 
countWords = 0
a=[]
for i in range(0,parentLength):
    if parentString[i] == subString[currentIndexSubString]:
        currentIndexSubString = currentIndexSubString + 1
        if currentIndexSubString == subStringLength:
            countWords = countWords + 1
            currentIndexSubString = 0
    else:
        a.append(parentString[i])
        currentIndexSubString = 0
        continue
    
print("WordsCount: " + str(countWords))
print("CountByFun: " + str(parentString.count(subString)))
print("a=" + ''.join(a))
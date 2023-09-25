parentString = "ellh htth djofiva hjjkh dwjepdfoh"
ch='h'
parentLength = len(parentString)
flag = -1
startIndex=0
endIndex=0

for i in range(0,parentLength):
    if parentString[i] == ch:
        #print("inside if - " + parentString[i] + " : " + ch + " i = " + str(i))
        if flag == -1:
            startIndex = i+1
            flag = 1
        elif flag == 1:
            endIndex = i-1
            #print("need to print string - " + str(startIndex) + " : " +  str(endIndex))
            flag = -1
            print(str(parentString[startIndex:endIndex]), end ="\n")
            
    else:
        if flag == -1:
            continue
        
    
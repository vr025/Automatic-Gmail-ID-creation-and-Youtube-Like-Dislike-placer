import string

def OpenFile():
    userInputs = open("C:\\Users\\Vignesh\\Desktop\\python project\\code\\MainPackage\\HandyPackage\\UserInputs.txt","r")
    #print(str(userInputs.read()))
    datalist = []
    sendcontents = userInputs.read()
    samplelist = sendcontents.split("\n")
    #print(samplelist)
    j = len(samplelist)
    for i in range(j):
        samplelist1=samplelist[i].split("=",1)
        datalist.append(samplelist1[1])
    #print(datalist)
    userInputs.close()
    return datalist
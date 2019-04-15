import string

def splitvalues(locator):
    secondlist =[]
    mainlist = []
    locators = open("C:\\Users\\Vignesh\\Desktop\\python project\\code\\MainPackage\\HandyPackage\\Locators.txt", "r")
    #print(str(locators.read()))
    locatorsFull = locators.read()
    samplelist = locatorsFull.split("\n")
    #print(samplelist)
    length = len(samplelist)

    for i in range(length):
        if locator in samplelist[i]:
            secondlist.append(samplelist[i])

    #print(secondlist)
    j= len(secondlist)
    for i in range(j):
        thirdlist = secondlist[i].split("= ")
        mainlist.append(thirdlist[1])

    return mainlist
    locators.close()
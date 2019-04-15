from selenium import webdriver
import HandyPackage.OpenBrowser as openBR
import HandyPackage.FetchInputs as userinputs
import HandyPackage.Splitvalues as splits
import HandyPackage.Operation as Op
import time

class ExecuteAuto():

    def ExecuteOperation(self):
        global datalist
        global driver
        datalist = userinputs.OpenFile()
        print(datalist)
        driver = None


    def DoAction(self):
        driver = openBR.openbrowser(datalist[0])
        driver.get(datalist[1])
        driver.implicitly_wait(5)
        currentURL = driver.current_url

        action = datalist[2]

        mainlist = splits.splitvalues("SignIN ")
        Op.operations(mainlist,"click",driver)
        mainlist = splits.splitvalues("EmailID ")
        Op.operations(mainlist, "enter", driver, "oviya.vr026")
        mainlist = splits.splitvalues("EmailNext ")
        Op.operations(mainlist, "click", driver)
        mainlist = splits.splitvalues("Password ")
        Op.operations(mainlist, "enter", driver, "lioninden",10)
        mainlist = splits.splitvalues("PasswordNext ")
        Op.operations(mainlist, "click", driver)

        time.sleep(15)

        currentURL1 = driver.current_url
        print(currentURL1)
        print(currentURL)

        if currentURL1 != currentURL:
            mainlist = splits.splitvalues("SelectCity ")
            Op.operations(mainlist, "click", driver)
            mainlist = splits.splitvalues("CityEnter ")
            Op.operations(mainlist, "enter", driver,"chennai",10)
            mainlist = splits.splitvalues("CityNext ")
            Op.operations(mainlist, "click", driver)
            mainlist = splits.splitvalues("DoneOption ")
            Op.operations(mainlist, "click", driver)

        if action == "like":
            mainlist = splits.splitvalues("LikeClick ")
            Op.operations(mainlist, "click", driver,15)
        else:
            mainlist = splits.splitvalues("DisClick ")
            Op.operations(mainlist, "click", driver,15)
        time.sleep(10)
        driver.close()



EA = ExecuteAuto()
EA.ExecuteOperation()
EA.DoAction()

#sp = splits.splitvalues("LikeCheck ")
#for i in sp:
    #print(i)





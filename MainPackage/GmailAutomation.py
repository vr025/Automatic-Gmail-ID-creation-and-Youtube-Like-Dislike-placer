from selenium import webdriver
import HandyPackage.OpenBrowser as openBR
import HandyPackage.FetchInputs as userinputs
import HandyPackage.Splitvalues as splits
import HandyPackage.Operation as Op


class ExecuteGmail():

    def ExecuteGmailOperation(self):
        global driver
        global datalist
        driver = None
        datalist = userinputs.OpenFile()
        print(datalist)

    def Action(self):
        driver = openBR.openbrowser(datalist[0])
        driver.get(datalist[3])
        driver.implicitly_wait(5)
        currentURL = driver.current_url
        print(currentURL)

        mainlist = splits.splitvalues("FirstName ")
        Op.operations(mainlist,"enter",driver,"OV")
        mainlist = splits.splitvalues("LastName ")
        Op.operations(mainlist, "enter", driver, "AV7")
        mainlist = splits.splitvalues("GmailAddress ")
        Op.operations(mainlist, "enter", driver, "ooviaarv7")
        mainlist = splits.splitvalues("CreatePassword1 ")
        Op.operations(mainlist, "enter", driver, "lioninden")
        mainlist = splits.splitvalues("ConfirmPassword2 ")
        Op.operations(mainlist, "enter", driver, "lioninden")
        mainlist = splits.splitvalues("Submit ")
        Op.operations(mainlist, "click", driver)
        mainlist = splits.splitvalues("MonthSelect ")
        Op.operations(mainlist, "click", driver)
        mainlist = splits.splitvalues("MonthClick ")
        Op.operations(mainlist, "click", driver)
        mainlist = splits.splitvalues("DaySelect ")
        Op.operations(mainlist, "enter", driver, "12")
        mainlist = splits.splitvalues("YearSelect ")
        Op.operations(mainlist, "enter", driver, "1990")
        mainlist = splits.splitvalues("GenderSelect ")
        Op.operations(mainlist, "click", driver)
        mainlist = splits.splitvalues("GenderClick ")
        Op.operations(mainlist, "click", driver)

       # mainlist = splits.splitvalues("SecondSelect ")
       # Op.operations(mainlist, "click", driver)
        mainlist = splits.splitvalues("SecondSelect ")
        Op.operations(mainlist, "click", driver)
        mainlist = splits.splitvalues("AgreeSelect ")
        Op.operations(mainlist, "click", driver)
       # mainlist = splits.splitvalues("ContinueSelect ")
       # Op.operations(mainlist, "click", driver)



EGA = ExecuteGmail()
EGA.ExecuteGmailOperation()
EGA.Action()


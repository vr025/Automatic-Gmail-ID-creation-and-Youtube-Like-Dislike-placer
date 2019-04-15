from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import time

def operations(mainlist,action,driver,value=" ",s=1):
    length = len(mainlist)
    element = None
    count1 = 0

    for i in range(length):
        try:
            time.sleep(s)
            element = driver.find_element(By.XPATH,mainlist[i])
            if element is not None:
                print(i)
                print(mainlist[i])
                break
        except:
            count1 = count1 + 1
            print("Node not found")
    print(i)
    print(count1)
    print(length)
    if count1 == length:
        print("Try adding new path")
    elif action == "click":
        time.sleep(s)
        element.click()
    elif action == "enter":
        element.send_keys(value)
    else:
        print("No definite action")



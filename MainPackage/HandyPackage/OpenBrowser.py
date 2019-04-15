
from selenium import webdriver
import os


def openbrowser(browserType="gc"):
    driver = None
    driverLocation = "C:\\Users\\Vignesh\\Desktop\\python project\\code\\MainPackage\\chromedriver_win32\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverLocation
    if browserType == "ff":
        driver = webdriver.Firefox()
    elif browserType == "gc":
        driver = webdriver.Chrome(driverLocation)
    else:
        print("Please give proper browser type ")
    return driver
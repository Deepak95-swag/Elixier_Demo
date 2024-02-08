from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
import base_Page as BasePage
from utils.Locators import *
import salesInvoiceAutomationSteps
import customerDetailsAutomationSteps
import readExcelfile

def start(config_reader, key):
    #Read Excel File
    print("Start Reading Excel File")
    key_value_dict,alistOfKeyColumn = readExcelfile.ReadExcelPath(key)
    print("Completed Reading Excel File")

    #setUpBrowser
    print("SetUp Browser")
    driver,waitDriver = setUpBrowser()
    print("Browser SetUp Completed")

    #Login Page
    print("Start Login Page")
    stepsMoveToElixirLoginPage(key,driver,waitDriver,config_reader)
    print("End Login Page")

    # Move to Sales Management Menu
    print("Start Move to Sales Management Menu")
    stepToSalesManagementMenu(waitDriver)
    print("End Move to Sales Management Menu")

    # Move to Sales Invoice Sub Menu
    print("Start Move to Sales Invoice Sub Menu")
    stepSalesInvoiceSubMenu(waitDriver)
    print("End Move to Sales Invoice Sub Menu")

    # Automate
    print("Start Sales Invoice Automating Entry")
    salesInvoiceAutomationSteps.stepsStartAutomateSalesInvoiceEntry(
        waitDriver, alistOfKeyColumn, key_value_dict,
    )
    print("End Sales Invoice Automating Entry")

    print("Start Customer details Automating Entry")
    customerDetailsAutomationSteps.stepsStartAutomateCustomerDetailsEntry(
        waitDriver, alistOfKeyColumn, key_value_dict,
    )
    print("End Customer details Automating Entry")


def setUpBrowser():
    try:
        Chrome_driver_path = ChromeDriverManager().install()
        print(Chrome_driver_path)
        print(
        "Try to get the path of the Chrome driver executable without downloading it again"
        )
    except:
        print(Chrome_driver_path)
        # If the driver is not already installed, download and install it
        Chrome_driver_path = ChromeDriverManager().install()
        print("If the driver is not already installed, download and install it")

    #Create a service instance using chrome driver executable path
    s = Service(executable=Chrome_driver_path)
    print("Create a Service instance using the Chrome driver executable path")

    #Create a chrome webdriver instance using the service
    driver = webdriver.Chrome(service=s)

    driver.maximize_window()
    waitDriver = WebDriverWait(driver, 30)
    return driver, waitDriver

def stepsMoveToElixirLoginPage(Key,driver,waitDriver,config_reader):
    driver.get(config_reader.get_ElixirURL(Key))
    time.sleep(5)

    # Enter Valid UserName
    userNameFieldLocator = BasePage.findElementByXpath(
        waitDriver,LoginPageLocators.userNameField
    )
    userNameFieldLocator.send_keys(config_reader.get_ElixirUserName(Key))
    time.sleep(2)

    # Enter Valid Password
    passwordFieldLocator = BasePage.findElementByXpath(
        waitDriver,LoginPageLocators.passWordField
    )
    passwordFieldLocator.send_keys(config_reader.get_ElixirPassword(Key))
    time.sleep(2)

    #click Login Button
    loginBtnLocator = BasePage.findElementByXpath(
        waitDriver,LoginPageLocators.loginBtn
    )
    loginBtnLocator.click()


def stepToSalesManagementMenu(waitdriver):
    #click on Sales Management Menu
    salesManagementMenuLocator = BasePage.findElementByXpath(
        waitdriver,MenuLocators.salesManagementMenu
    )
    salesManagementMenuLocator.click()

def stepSalesInvoiceSubMenu(waitDriver):
    #Click on SalesInvoice Sub Menu
    salesInvoiceSubMenuLocator = BasePage.findElementByXpath(
        waitDriver,MenuLocators.salesInvoiceSubMenu
    )
    salesInvoiceSubMenuLocator.click()

    loggedInAs = BasePage.findElementByXpath(
        waitDriver,salesInvoicePageLocators.loggedInAs
    )
    print("Logged in as:" + loggedInAs.text)
   
   # Verify click
    BasePage.findElementByXpath(waitDriver,MenuLocators.salesInvoiceLabel)
    BasePage.findElementByXpath(waitDriver,salesInvoicePageLocators.CreateNewBtn)
    time.sleep(2)


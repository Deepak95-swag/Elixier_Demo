from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import base_Page as BasePage
from utils.Locators import *


def stepsStartAutomateSalesInvoiceEntry(
    waitDriver,
    alistOfKeyColumn,
    key_value_dict,
):
    
    createNewBtnLocator = BasePage.findElementByXpath(
        waitDriver, salesInvoicePageLocators.CreateNewBtn
    )

    createNewBtnLocator.click()

# Iterate the branch ID or Key Column List
    for uniqueKey in alistOfKeyColumn:
        print(f"UniqueKey value is '{uniqueKey}'")
        print(uniqueKey)
        
        # Enter Branch ID       
    
    BasePage.enterOrSelectValueInGivenFields(
            salesDetailsFieldLocators.branchId,
            key_value_dict,
            uniqueKey,
            "Branch Id.",
            waitDriver,
        )
    
      #Document Date
    
    BasePage.enterOrSelectValueInGivenFields(
            salesDetailsFieldLocators.documentDate,
            key_value_dict,uniqueKey,
            "Document Date",waitDriver
        )
    
    #Document Date field Warning Alert

    warningAlert = BasePage.warningAlert(
    waitDriver,salesDetailsFieldLocators.warningAlert
    )
    warningAlert.click()
    
    #Reverse Charge Y/N ?

    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.reverseChargeYesOrNo,
        key_value_dict,uniqueKey,
        "Reverse Charge Y/N ?",waitDriver
    )

    # Invoice for
    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.invoiceFor,
        key_value_dict,uniqueKey,
        "Invoice for",waitDriver
    )
    
    # Voucher Type
    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.voucherType,
        key_value_dict,uniqueKey,
        "Voucher Type",waitDriver
    )

    #Type of pay
    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.typeOfPay,
        key_value_dict,uniqueKey,
        "Type of Pay",waitDriver
    )

    #Sales Type
    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.salesType,
        key_value_dict,uniqueKey,
        "Sales Type",waitDriver
    )
    
    #Invoice Type
    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.invoiceType,
        key_value_dict,uniqueKey,
        "Invoice Type",waitDriver
    )

    #tcsYesOrNo ?
    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.tcsYesOrNo,
        key_value_dict,uniqueKey,
        "TCS Y/N?",waitDriver
    )
    """""
    #Tax Applicable ?
    BasePage.enterOrSelectValueInGivenFields(
        salesDetailsFieldLocators.taxApplicable,
        key_value_dict,uniqueKey,
        "Tax Applicable",waitDriver
    )
    """
    

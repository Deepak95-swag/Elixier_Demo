import salesInvoiceAutomationSteps
import time
import base_Page as BasePage
from utils.Locators import *
import salesInvoiceAutomationSteps


def stepsStartAutomateCustomerDetailsEntry(waitDriver,alistOfKeyColumn,key_value_dict):

    for uniqueKey in alistOfKeyColumn:
        print(f"UniqueKey value is '{uniqueKey}'")
        print(uniqueKey)

     # Enter Customer Id.(Right Click for More Options)

    BasePage.enterOrSelectValueInGivenFields(
            customerDetailsFieldLocators.customerId,
            key_value_dict,
            uniqueKey,
            "Customer Id.(Right Click for More Options)",
            waitDriver
    )

    # credit days exceeded for the customer, do you want to proceed ? Warning Alert
    
    warningAlert = BasePage.warningAlert(
    waitDriver,salesDetailsFieldLocators.warningAlert
    )
    warningAlert.click()

     # Enter Delivery At./Service Rendered At. / State

    BasePage.enterOrSelectValueInGivenFields(
        customerDetailsFieldLocators.deliveryAt,
        key_value_dict,uniqueKey,
        "Delivery At./Service Rendered At. / State",
        waitDriver
    )
     # Enter Customer PO. No

    BasePage.enterOrSelectValueInGivenFields(
       customerDetailsFieldLocators.customerPoNo,
       key_value_dict,uniqueKey,
       "Customer PO. No",waitDriver
    )

    time.sleep(10)
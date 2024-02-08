from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from utils.Locators import *
import os
from utils.config_Reader import ConfigReader


def enterOrSelectValueInGivenFields(
    locator, key_value_dict, uniqueKey, fieldIdentity, waitdriver
):
    element = findElementByXpath(waitdriver, locator)

    element.click()
    time.sleep(0.5)
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.BACKSPACE)
    time.sleep(0.5)
    element.send_keys(
        str(getDesiredKeyAndColumn(key_value_dict, uniqueKey, fieldIdentity))
    )
    time.sleep(0.5)
    element.send_keys(Keys.ENTER)
    time.sleep(0.5)
    element.send_keys(Keys.TAB)


def findElementByXpath(waitDriver, locator):
    element = waitDriver.until(EC.element_to_be_clickable((By.XPATH, locator)))
    return element


def currentExcelPath(__file__, key):
    config_reader = ConfigReader()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    excelValuePath = os.path.join(current_dir, config_reader.get_ExcelFilePath(key))
    print(excelValuePath)
    return excelValuePath


def findElements(waitDriver, locator):
    element = waitDriver.until(EC.visibility_of_element_located((By.ID, locator)))
    return element

def warningAlert(waitDriver,locator):
    element = waitDriver.until(EC.element_to_be_clickable((By.XPATH,locator)))
    
    return element


def getDesiredKeyAndColumn(key_value_dict, desired_key, desired_column):
    if desired_key in key_value_dict:
        # Check if the specified column exists in the values for the key
        if desired_column in key_value_dict[desired_key]:
            value_for_desired_column = key_value_dict[desired_key][desired_column]
            print(
                f"Value for key '{desired_key}' in column '{desired_column}': {value_for_desired_column}"
            )
            return value_for_desired_column
        else:
            print(f"Column '{desired_column}' not found for key '{desired_key}'.")
    else:
        print(f"Key '{desired_key}' not found in the dictionary.")

import pandas as pd
from selenium import webdriver
import base_Page as BasePage


# Read Excel file
def ReadExcelPath(key):
    # excel_file_path = "E:\\Automation\\elixirSalesAutomation\\files\\values.xlsx"
    excelValuePath = BasePage.currentExcelPath(__file__,key)

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excelValuePath)

    # Use the first column as the key and the next 10 columns as values
    key_column = df.columns[0]
    value_columns = df.columns[1:]

    # Create a dictionary with key-value pairs
    key_value_dict = df.set_index(key_column)[value_columns].to_dict(orient="index")

    # Extract the values from the first column and convert it to a list
    alistOfKeyColumn = df.iloc[:,0].tolist()

    print("List from the first column:")
    print(alistOfKeyColumn)

    # Specify the key and column you want to retrieve
    desired_key = "U001"

    columnValue1 = BasePage.getDesiredKeyAndColumn(
        key_value_dict, desired_key, "Reverse Charge Y/N ?"
    )
    print(columnValue1)

    columnValue2 = BasePage.getDesiredKeyAndColumn(
        key_value_dict, desired_key, "Branch Id."
    )
    print(columnValue2)

    #print(df.iloc[0:])

    return key_value_dict, alistOfKeyColumn

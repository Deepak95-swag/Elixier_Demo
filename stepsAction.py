import readExcelfile as ReadExcel
import automationpage as Ap
from utils.config_Reader import ConfigReader

config_reader = ConfigReader()

class elixirAutomation:
    def __init__(self):
        print("Start Automation")
        self.runAutomation()

    def runAutomation(self):
        print("run Automation")

        # excel read
        ##key = config_reader.get_envKey("env")
        ##key_value_dict, alistOfKeyColumn = ReadExcel.ReadExcelPath(key)
        ##print(key_value_dict, alistOfKeyColumn)

        # browser setup
        key = config_reader.get_envKey("env")
        print(key)
        Ap.start(config_reader,key)
        print("Passed Automation page")
        
        # automation

        
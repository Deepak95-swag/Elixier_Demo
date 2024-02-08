
from configparser import ConfigParser

class ConfigReader:
    def __init__(self,config_file="config.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_ElixirURL(self,key):
        return self.config.get("elixirbsWebUrl", key)
    
    def get_ElixirUserName(self,key):
        return self.config.get("elixirbsUserName", key)
    
    def get_ElixirPassword(self,key):
        return self.config.get("elixirbsPassword", key)
    
    def get_ExcelFilePath(self,key):
        return self.config.get("pathOfExcelFile",key)
    
    def get_envKey(self,key):
        return self.config.get("envKey",key)


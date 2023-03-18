#which will read the ini file[common data]
import configparser
         #package      #class
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class readConfig:
    @staticmethod #when we create static method we no need to create the object of class, we directly use the class name
    def getApplicationURL():
        url = config.get("Common Information","baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("Common Information", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("Common Information","password")
        return password
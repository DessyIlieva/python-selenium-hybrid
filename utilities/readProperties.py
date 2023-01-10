import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations/config.ini')

class ReadConfig():
    
    @staticmethod
    def getApplicationURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        usernameData = config.get('common data', 'usernameData')
        return usernameData

    @staticmethod
    def getPassword():
        passwordData = config.get('common data', 'passwordData')
        return passwordData

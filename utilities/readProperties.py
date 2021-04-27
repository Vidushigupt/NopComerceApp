import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('Common Data', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        userEmail = config.get('Common Data', 'userEmail')
        return userEmail

    @staticmethod
    def getPassword():
        password = config.get('Common Data', 'password')
        return password

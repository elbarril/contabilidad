from model.Constants import APP_NAME

class Menu:
    def __init__(self):
        self.__appName = APP_NAME
        
    def getAppName(self):
        return self.__appName
from model.Constants import APP_NAME, YEAR, DEFAULT_USER
from model.Constants import HELP_TEXT, HELP_ENABLED_DEFAULT
class Menu():
    __title = APP_NAME + " " + YEAR
    __helpEnabled = HELP_ENABLED_DEFAULT
    __help = HELP_TEXT
    
    def getHeader(self, user = DEFAULT_USER):
        header = self.__title + " - " +  user
        return header

    def enableHelp(self):
        self.__helpEnabled = True
        
    def disableHelp(self):
        self.__helpEnabled = False

    def isHelpEnabled(self):
        return self.__helpEnabled
    
    def getHelp(self):
        return self.__help
from model.Constants import APP_NAME
import datetime

class Menu():
    __title = ''
    __isHelp = ''
    
    def setTitle(self, user):
        year = str(datetime.datetime.now().year)
        self.__title = f"{APP_NAME} {year} - {user}"
        
    def getTitle(self):
        return self.__title
    
    def setIsHelp(self, isHelp):
        self.__isHelp = isHelp
        
    def isHelp(self):
        return self.__isHelp
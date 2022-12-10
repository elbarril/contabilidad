from model.Menu import Menu
from console.MenuConsole import MenuConsole
import datetime
from model.Constants import INSTALL_SUCCESS

class MenuController():
    def __init__(self):
        self.__menuModel = Menu()
        self.__menuView = MenuConsole()
        self.__today = datetime.datetime.now()
        
    def run(self, message, userName):
        self.__menuView.clearAndShow(userName, self.__menuModel.getAppName(), self.__today.year)
        if message:
            self.__menuView.show(message)
            
    def close(self):
        self.__menuView.clear()
    
    def installMessage(self, message):
        self.__menuView.clearConsole()
        if isinstance(message, list):
            for m in message:
                self.__menuView.show(m)
        else:
            self.__menuView.show(message)
        self.__menuView.show(INSTALL_SUCCESS)
        self.__menuView.pressEnterToContinue()
        
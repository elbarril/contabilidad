from app.MenuController import MenuController
from app.ActionHandlerController import ActionHandlerController
from database.SQL3 import SQL3
from model.Constants import EXIT_INPUTS

class Controller(ActionHandlerController):
    __userInput=''
    __userName = ''
    
    def __init__(self):
        self.__sql3 = SQL3()
        self.__menu = MenuController()
        self.__install()
    
    def __runMenu(self, response, userName):
        self.__menu.run(response, userName)
        self.__userInput = input('')
    
    def __install(self):
        responseTables = self.__sql3.initTables()
        responseUser = self.__sql3.initUser()
        self.__userName = self.__sql3.getUserName()
        self.__menu.installMessage([responseTables, responseUser])
    
    def run(self):
        while not self.__userInput in EXIT_INPUTS:
            response = self.runAction(self.__sql3, self.__userInput)
            self.__runMenu(response, self.__userName)
        
        self.__exit()
    
    def __exit(self):
        self.__sql3.closeConnection()
        self.__menu.close()
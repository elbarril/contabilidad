from model.Menu import Menu
from console.MenuConsole import MenuConsole
from database.Database import Database
from model.Constants import EXIT_INPUTS, HELP_INPUTS, ACTIONS_INPUTS, CLEAR_INPUTS
from model.Constants import ACTIONS

class Controller():
    __input=''
    def __init__(self):
        self.__db = Database()
        self.__menu = Menu()
        self.__menuView = MenuConsole(self.__menu)
    
    def run(self):
        response = self.__db.install()

        self.__menu.setTitle(self.__db.getUser())
        self.__menuView.update(response)

        while not self.__input in EXIT_INPUTS:
            response = self.__evaluateInput()
            if response:
                self.__menuView.update(response)
            else:
                self.__menuView.update()
            self.__input = input('>')
            
        self.__exit()
    
    def __exit(self):
        self.__db.closeConnection()
        self.__menuView.close()
        
    def __evaluateInput(self):
        if self.__input:
            if self.__input in HELP_INPUTS:
                self.__menu.setIsHelp(True)
            elif self.__input in ACTIONS_INPUTS:
                values = self.__requestValues(ACTIONS[self.__input])
                response = self.__db.execute(self.__input, values)
                return response
            elif self.__input in CLEAR_INPUTS:
                self.__menu.setIsHelp(False)
                
    def __requestValues(self, action):
        values = []
        if action["query"] == "INSERT":
            self.__menuView.update(f"New record for {action['data']['table']} table")
            for column in action["data"]["columns"]:
                value = input(f"{column}: ")
                values.append(value)
                
        return values
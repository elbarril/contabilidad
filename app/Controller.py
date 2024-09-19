from model.Menu import Menu
from console.MenuConsole import MenuConsole
from database.Database import Database
from model.Constants import KEY_SHORTCUT_EXIT, KEY_SHORTCUT_HELP, KEY_SHORTCUT_CLEAR

class Controller():
    __input=''

    def __init__(self):
        self.__db = Database()
        self.__menu = Menu()
        self.__menuView = MenuConsole(self.__menu)
    
    def run(self):
        self.__db.install()

        while not self.__input in KEY_SHORTCUT_EXIT:
            response = self.__performInputAction()
            if response:
                self.__menuView.refresh(response)
            else:
                self.__menuView.refresh()
            self.__input = input('>')
        
        self.__menuView.close()
        
    def __performInputAction(self):
        pass
                
    def __requestValues(self, action):
        values = []
        if action["action"] == "add_record":
            self.__menuView.update(f"New record for {action['data']['table']} table")
            for column in action["data"]["columns"]:
                value = input(f"{column}: ")
                values.append(value)
                
        return values
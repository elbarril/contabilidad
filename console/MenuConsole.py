from console.WindowsOS import WindowsOS
from model.Constants import PRESS_ENTER_TO_CONTINUE, HELP
class MenuConsole(WindowsOS):
    def __init__(self, model):
        self.__model = model
    
    def close(self):
        self.clearConsole()
    
    def __clear(self):
        self.clearConsole()
        self.__showTitle()
        if self.__model.isHelp():
            self.__print(HELP)
        
    def __showTitle(self):
        self.__print(self.__model.getTitle())
    
    def __wait(self):
        input(PRESS_ENTER_TO_CONTINUE)
        self.__clear()
    
    def __print(self, data):
        if isinstance(data, str):
            print(data.capitalize())
        elif isinstance(data, dict):
            for item in data.items():
                print(str(item).capitalize())
        elif isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                print(str(item).capitalize())
        else:
            print(str(data).capitalize())
            
    def update(self, *messages):
        self.__clear()
            
        if messages:
            isMessage = True
            for message in messages:
                if not message is None:
                    if len(message):
                        self.__print(message)
                    else:
                        isMessage = False
            
            if isMessage:
                self.__wait()
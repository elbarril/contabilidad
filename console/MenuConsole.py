from console.WindowsOS import WindowsOS
from model.Constants import PRESS_ENTER_TO_CONTINUE

class MenuConsole(WindowsOS):
    def show(self, message):
        if isinstance(message, list):
            for m in message:
                self.__printData(m)
        elif len(message):
            self.__printData(message)
        
    def clearAndShow(self, userName, appName, year ):
        self.clearConsole()
        self.__printData(userName, appName, str(year))
    
    def clear(self):
        self.clearConsole()
    
    def pressEnterToContinue(self):
        input(PRESS_ENTER_TO_CONTINUE)
    
    def __printData(self, *data):
        for d in data:
            if not d is None:
                if len(d):
                    print(d.capitalize())
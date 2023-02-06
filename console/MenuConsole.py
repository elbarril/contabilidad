from console.WindowsOS import WindowsOS
from model.Constants import PRESS_ENTER_TO_CONTINUE
class MenuConsole(WindowsOS):
    def __init__(self, menu):
        self.__header = menu.getHeader()
        self.__isHelpEnabled = menu.isHelpEnabled()
        self.__helpText = menu.getHelp()
    
    def close(self):
        self.clearConsole()
    
    def showHeader(self):
        self.render(self.__header)

    def showHelp(self):
        self.render(self.__helpText)

    def showMessages(self, *messages):
        for message in messages:
            self.render(message)

    def showPressEnterMessage(self):
        input(PRESS_ENTER_TO_CONTINUE)

    def refresh(self, *messages):
        self.clearConsole()
        self.showHeader()
        if any(messages):
            self.showMessages(messages)
            self.showPressEnterMessage()
        if  self.__isHelpEnabled:
            self.showHelp()

    def render(self, data):
        print(data)
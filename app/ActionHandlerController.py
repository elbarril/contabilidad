from model.Constants import ACTIONS
from model.Action import Action
class ActionHandlerController:
    __data = {}
    def runAction(self, sql3, action):
        if action:
            self.__data = ACTIONS[action]["data"]
            if not ACTIONS[action]["query"] is 'select':
                self.__data["values"] = []
                for column in self.__data["columns"]:
                    self.__data["values"].append(input(f"Insert value for '{column}'"))
                
            return Action(sql3, ACTIONS[action]["query"], self.__data).execute()
        else:
            return ACTIONS['h']
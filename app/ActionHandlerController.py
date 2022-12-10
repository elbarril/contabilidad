from model.Constants import ACTIONS, HELP

class ActionHandlerController:
    def runAction(self, action):
        if action in ACTIONS:
            return ACTIONS[action]
        else:
            return HELP
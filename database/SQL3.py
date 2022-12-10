import sqlite3 as sql3
from model.Constants import DB_NAME, DB_PATH
from database.AccountDatabase import AccountDatabase
from database.UserDatabase import UserDatabase

class SQL3:
    def __init__(self):
        self.__connection = sql3.connect(DB_PATH + DB_NAME)
        self.__database = {
            "user" : UserDatabase(self.__connection),
            "account": AccountDatabase(self.__connection)
        }
        
    def getDatabase(self, key):
        return self.__database[key]
    
    def closeConnection(self):
        self.__connection.close()
        
    def initTables(self):
        response = []
        for table in self.__database:
            tableResponse = self.__database[table].table()
            if not tableResponse is None:
                response.append(tableResponse)
        return response
    
    def initUser(self):
        return self.__database["user"].setUserName()
        
    def getUserName(self):
        return self.__database["user"].getUserName()
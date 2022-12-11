from database.Database import Database
from model.Constants import DB_USER_TABLE
from model.Constants import DB_USER_TABLE_COLUMNS
from model.Constants import INSERT_NAME, USER_NAME_SUCCESS
from model.Constants import DB_TABLE_CREATED

class UserDatabase(Database):
    def __init__(self, connection):
        super().__init__(connection)
        
    def table(self):
        if not self.tableExists(DB_USER_TABLE):
            self.createTable(DB_USER_TABLE, DB_USER_TABLE_COLUMNS)
            return f"{DB_USER_TABLE} {DB_TABLE_CREATED}"
            
    def add(self, name):
        self.insert(DB_USER_TABLE, {"name": name})
        
    def setUserName(self):
        if not self.hasRecords(DB_USER_TABLE):
            self.add(input(INSERT_NAME))
            return USER_NAME_SUCCESS
        else:
            return None

    def getUserName(self):
        if self.hasRecords(DB_USER_TABLE):
            return self.retriveFirstRecord(DB_USER_TABLE)[1]
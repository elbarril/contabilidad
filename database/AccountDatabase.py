from database.Database import Database
from model.Constants import DB_ACCOUNT_TABLE
from model.Constants import DB_ACCOUNT_TABLE_COLUMNS
from model.Constants import DB_TABLE_CREATED

class AccountDatabase(Database):
    def __init__(self, connection):
        super().__init__(connection)
        
    def table(self):
        if not self.tableExists(DB_ACCOUNT_TABLE):
            self.createTable(DB_ACCOUNT_TABLE, DB_ACCOUNT_TABLE_COLUMNS)
            return f"{DB_ACCOUNT_TABLE} {DB_TABLE_CREATED}"
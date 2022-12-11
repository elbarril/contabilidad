from database.Database import Database
from model.Constants import DB_SPENDS_TABLE
from model.Constants import DB_SPENDS_TABLE_COLUMNS
from model.Constants import DB_TABLE_CREATED

class SpendsDatabase(Database):
    def __init__(self, connection):
        super().__init__(connection)
        
    def table(self):
        if not self.tableExists(DB_SPENDS_TABLE):
            self.createTable(DB_SPENDS_TABLE, DB_SPENDS_TABLE_COLUMNS)
            return f"{DB_SPENDS_TABLE} {DB_TABLE_CREATED}"
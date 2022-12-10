class Database:
    def __init__(self, connection):
        self.__connection=connection
        
    def tableExists(self, table):
        cursor = self.__connection.cursor()
        table = cursor.execute(f"SELECT name FROM sqlite_master WHERE name='{table}'").fetchone()
        return True if table else False
        
    def createTable(self, table, columns):
        cursor = self.__connection.cursor()
        cursor.execute(f"CREATE TABLE {table}{columns}")
        
    def insert(self, table, item):
        cursor = self.__connection.cursor()
        columns = ""; values = ""
        for key in item:
            columns = columns + ("," if columns else '') + key
            values = values + ("," if values else '') + "'" + item[key] + "'"
        query = f"INSERT INTO {table} ({columns}) VALUES ({values});"
        cursor.execute(query)
        self.__connection.commit()
        
    def hasRecords(self, table):
        cursor = self.__connection.cursor()
        record = cursor.execute(f"SELECT * FROM {table}").fetchone()
        return True if record else False
    
    def retriveFirstRecord(self, table):
        cursor = self.__connection.cursor()
        record = cursor.execute(f"SELECT * FROM {table}").fetchone()
        return record
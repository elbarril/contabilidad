import sqlite3 as sql3
from model.Constants import DB_PATH, DB_NAME
from model.Constants import DB, INSTALL_SUCCESS
class Database():
    __user = ''
    def __init__(self):
        self.__connection = sql3.connect(DB_PATH + DB_NAME)
        self.__execute = {
            "list_records": self.__executeSelectFrom,
            "list_records_filtered": self.__executeSelectFromWhere,
            "create_table": self.__executeCreateTable,
            "add_record": self.__executeInsertInto
        }

    def install(self):
        self.__execute["create_table"]("account", "id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255)")
        self.__execute["create_table"]("user", "id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), amount INTEGER")
        return INSTALL_SUCCESS
    
    def getUser(self):
        return self.__user
        
    def __executeSelectFrom(self, table, columns):
        cursor = self.__connection.cursor()
        query = f"SELECT {columns} FROM {table}"
        cursor.execute(query).fetchall()
        self.__connection.close()
        
    def __executeSelectFromWhere(self, table, columns, filter):
        cursor = self.__connection.cursor()
        query = f"SELECT {columns} FROM {table} WHERE {filter}"
        cursor.execute(query).fetchall()
        self.__connection.close()
    
    def __executeCreateTable(self, table, columns):
        cursor = self.__connection.cursor()
        db_table = cursor.execute(f"SELECT * FROM sqlite_master WHERE name='{table}'").fetchone()
        if not db_table:
            query = f"CREATE TABLE {table} ({columns})"
            cursor.execute(query)
            self.__connection.commit()
            self.__connection.close()
     
    def __executeInsertInto(self, table, columns, values):
        cursor = self.__connection.cursor()
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cursor.execute(query).fetchall()
        self.__connection.commit()
        self.__connection.close()
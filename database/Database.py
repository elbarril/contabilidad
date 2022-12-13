import sqlite3 as sql3
from model.Constants import DB, ACTIONS, STRINGS, INSTALL_SUCCESS
class Database():
    __user = ''
    def __init__(self):
        self.__connection = sql3.connect(DB["path"] + DB["name"])
        self.__methods = {
            "SELECT": self.__sqlSelect,
            "CREATE": self.__sqlCreate,
            "INSERT": self.__sqlInsert,
            "UPDATE": self.__sqlUpdate,
            "DELETE": self.__sqlDelete
        }
    
    def execute(self, key, values):
        cursor = self.__connection.cursor()
        method = ACTIONS[key]["query"]
        table = ACTIONS[key]["data"]["table"]
        columns = ACTIONS[key]["data"]["columns"]
        if len(values):
            query = self.__methods[method](table=table, columns=columns, values=values)
        else:
            query = self.__methods[method](table=table, columns=columns)
        print(query)
        response = cursor.execute(query).fetchall()
        self.__connection.commit()
        return response if len(response) else "Nothing found"

    def install(self):
        response = []
        cursor = self.__connection.cursor()
        
        for name, data in DB["tables"].items():
            query = self.__methods["SELECT"](table="sqlite_master", columns=["name"], filter=["name", name])
            table = cursor.execute(query).fetchone()
            if not table:
                query = self.__methods["CREATE"](table=name, columns=data["columns"])
                cursor.execute(query)
                response.append(f"{name} table created.")

        query = self.__methods["SELECT"]("user", ["name"])
        user = cursor.execute(query).fetchone()
        
        if not user:
            userName = input("Insert user name: ")
            query = self.__methods["INSERT"](table="user", columns=["name"], values=[userName])
            cursor.execute(query)
            self.__connection.commit()
            response.append("User created.")
            self.__user = userName
        else:
            self.__user = user[0]
            
        if len(response):
            response.append(INSTALL_SUCCESS)
            
        return response
        
    def getUser(self):
        return self.__user
        
    def __sqlSelect(self, table, columns, filter = None):
        sqlColumns = STRINGS["comma"].join(columns) if columns else "*"
        if filter:
            sqlFilter = filter[0] + STRINGS["equals"] + STRINGS["single_quotation"] + filter[1] + STRINGS["single_quotation"]
            return STRINGS["space"].join(["SELECT", sqlColumns, "FROM", table,"WHERE", sqlFilter])
        else:
            return STRINGS["space"].join(["SELECT", sqlColumns, "FROM", table])
    
    def __sqlCreate(self, table, columns):
        query = STRINGS["space"].join(["CREATE TABLE",table,STRINGS["open_parenthesis"]])
        for i, column in enumerate(columns):
            query = STRINGS["space"].join([query,STRINGS["space"].join([column["name"], column["type"]])])
            if "primarykey" in column.keys():
                query = STRINGS["space"].join([query,"PRIMARY KEY"])
            if "autoincrement" in column.keys():
                query = STRINGS["space"].join([query,"AUTOINCREMENT"])
            if "limit" in column.keys():
                query = STRINGS["space"].join([query,STRINGS["open_parenthesis"] + str(column["limit"]) + STRINGS["close_parenthesis"]])
            if i != len(columns) - 1:
                query = STRINGS["space"].join([query,STRINGS["comma"]])
        query =STRINGS["space"].join([query,STRINGS["close_parenthesis"]])
        return query   
     
    def __sqlInsert(self, table, columns, values):
        query = STRINGS["space"].join(["INSERT INTO",table,STRINGS["open_parenthesis"]])
        for i, column in enumerate(columns):
            if i == 0:
                query = STRINGS["space"].join([query,column])
            else:
                query = STRINGS["comma"].join([query,column])
        query = STRINGS["space"].join([query,STRINGS["close_parenthesis"],'VALUES',STRINGS["open_parenthesis"]])
        for i, value in enumerate(values):
            if i == 0:
                query = STRINGS["space"].join([query,STRINGS["single_quotation"],value,STRINGS["single_quotation"]])
            else:
                query = STRINGS["comma"].join([query,STRINGS["single_quotation"],value,STRINGS["single_quotation"]])
        query = STRINGS["space"].join([query,STRINGS["close_parenthesis"]])
        return query
        return f"INSERT INTO {table} ({columns[0]}) VALUES ('{values[0]}')" 
    
    def __sqlUpdate(self, columns, table, filter = None):
        pass
    
    def __sqlDelete(self, columns, table, filter = None):
        pass
    
    def closeConnection(self):
        self.__connection.close()
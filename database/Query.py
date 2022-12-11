from model.Constants import QUERIES, MODIFIERS

class Query:
    def __init__(self, connection, query, data):
        self.__connection = connection
        self.__data = data
        self.__query = query

    def execute(self):
        successMessage = [self.__getMessage(self.__query)]
        if self.__query == 'select':
            response = self.__connection.cursor().execute(self.__applyModifiersToQuery()).fetchall()
            successMessage = successMessage + response
        else:
            self.__connection.cursor().execute(self.__applyModifiersToQuery())
            self.__connection.commit()

        return successMessage
        
    def __applyModifiersToQuery(self):
        modifiers = {}
        query = QUERIES[self.__query]
        for dataIndex in self.__data:
            if isinstance(self.__data[dataIndex], list):
                if dataIndex == "values":
                    modifiers[MODIFIERS[dataIndex]] = self.__joinWithQuotes(dataIndex)
                else:
                    modifiers[MODIFIERS[dataIndex]] = self.__join(dataIndex)
            else:
                modifiers[MODIFIERS[dataIndex]] = self.__data[dataIndex]
        
        for key in modifiers:
            query = query.replace(key, modifiers[key])

        return query
    
    def __join(self, dataIndex):
        return ', '.join(self.__data[dataIndex])
    
    def __joinWithQuotes(self, dataIndex):
        dataWithQuotes = "'"
        dataWithQuotes = dataWithQuotes + "','".join(self.__data[dataIndex])
        dataWithQuotes = dataWithQuotes + "'"
        return dataWithQuotes
    
    def __getMessage(self, query):
        if query == 'insert':
            return f"{self.__query} method in {self.__data['table']} success!"
        elif query == "select":
            return f"List of {self.__data['table']}s:"
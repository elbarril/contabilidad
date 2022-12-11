class Action:
    def __init__(self, sql3, query, data):
        self.__query = sql3.getQuery(query, data)
        
    def execute(self):
        return self.__query.execute()
        
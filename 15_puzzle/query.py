class Query:
    def __init__(self, sql):
        self.sql = sql
    def GetQuery(self):
        return self.sql
    def SetQuery(self, sql):
        self.sql = sql
    
from query import Query
class DB:
    __instance = None
    def __init__(self):
        if DB.__instance is not None:
            raise Exception("Factory is a Singleton! Use get_instance()")
        else:
            DB.__instance = self
    @staticmethod
    def getInstance():
        if DB.__instance is None:
            DB()
        return DB.__instance
    def saveQuery(self, query):
        pass
    def loadQuery(self, query):
        pass
    def UpdateQuery(self, query):
        pass
    def DeleteQuery(self, query):
        pass
    def ExecuteQuery(self, query):
        pass
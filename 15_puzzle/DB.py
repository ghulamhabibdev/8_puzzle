class DB:
    __instance = None

    def __init__(self):
        if DB.__instance is not None:
            raise Exception("DB is Singleton!")
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

    def updateQuery(self, query):
        pass

    def deleteQuery(self, query):
        pass

    def executeQuery(self, query):
        pass

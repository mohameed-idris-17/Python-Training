# Example B: Database Connection (Abstraction)
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL Database"

class MongoDB(Database):
    def connect(self):
        return "Connected to MongoDB Database"

db1 = MySQLDatabase()
db2 = MongoDB()
print(db1.connect())
print(db2.connect())

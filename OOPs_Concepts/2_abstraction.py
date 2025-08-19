# Example B: Database Connection (Abstraction)
# What’s being abstracted: the concept of connecting to a database, defined by the connect method in the Database base class.
# What’s hidden: the specific details of how each database connection works; users don’t need to know the implementation.
# What’s exposed: a simple interface (connect) that all database types must provide, ensuring consistency.
# How it works conceptually: you interact with databases through a common method, while each subclass supplies its own connection logic.
# Why it matters: enables flexible switching between database types, reduces coupling, and enforces a contract for all database classes.
# One-liner for interview: “Abstraction defines a common way to connect, letting each database handle its own details behind the scenes.
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

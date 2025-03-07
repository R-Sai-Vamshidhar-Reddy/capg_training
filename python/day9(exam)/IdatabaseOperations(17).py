from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod    
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Insertion is done in SQL database")

    def update(self):
        print("Updation is done in SQL database")

    def delete(self):
        print("Deletion is done in SQL database")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Insertion is done in NoSQL database")

    def update(self):
        print("Updation is done in NOSQL database")

    def delete(self):
        print("Deletion is done in NoSQL database\n")

sql=SQLDatabase()
sql.insert()
sql.update()
sql.delete()

nosql=NoSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()
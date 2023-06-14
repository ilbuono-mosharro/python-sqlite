import sqlite3

class Database:
    """
    Is a class to manage the database.
    """
    def __init__(self, db_name):
        """ 
        The constructor takes only one argument which is the name of the database, 
        and self.connection is None and help us in the methods to create a connection with the database.
        """
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """
        This method initiates a connection to the database.
        """
        self.connection = sqlite3.connect(self.db_name)

    def disconnect(self):
        """
        This method close a connection to the database.
        """
        if self.connection:
            self.connection.close()

    def execute_cud_query(self, query, params=None):
        """
        This method takes 2 arguments the query, and other is the params which is none 
        and helps us to run a query to create, update and delete records.
        """
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        cursor.close()
        self.connection.commit()

    def execute_query_fetch(self, query):
        """
        This method takes 1 argument the query, 
        and helps us to run a query to fetch all the records from the table.
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return result
    

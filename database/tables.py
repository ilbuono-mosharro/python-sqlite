from core.settings import db

class Tables:
    """
    Is a class to manage the tables.
    """
    def __init__(self):
        """
        The constructor takes no arguments, we only have columns which is a list,
        which we need to keep track of the columns for the table
        """
        self.columns = []
        self.all_tables = []
        
    def retrieve_tables(self):
        """
        This methods allow to get all the tables from the database
        """
        results = db.execute_query_fetch("SELECT name FROM sqlite_master WHERE type='table'")
        for table in results:
            self.all_tables.append(''.join(table))
    
    def get_table(self, table_name):
        data = []
        results = db.execute_query_fetch(f"PRAGMA table_info({table_name})")
        for res in results:
            data.append(res[0:2])
        print(data)
        return data

    @classmethod
    def create(cls, table_name):
        """
        This methods take a table_name argument, and create a table in the database.
        """
        db.execute_cud_query(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT)")
        return cls
    
    def drop(self, table_name):
        """
        This methods drop the table from the database.
        """
        db.execute_cud_query(f"DROP TABLE {table_name}")

    def get_db_name(self):
        """
        This methods return the name of the database.
        """
        return str(db.db_name)
    
    def add_column_to_table(self, column):
        """
        This methods take one argument which is the name of the column and append to the list columns.
        """
        self.columns.append(column)




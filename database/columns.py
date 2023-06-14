from core.settings import db

class TablesColumn:
    """
    Is a class to manage the colums of table.
    """
    def __init__(self, col_name, data_type):
        """
        This constructor take 2 arguments, the name of the column and the datatype.
        """
        self.col_name = col_name
        self.data_type = data_type

    def add_column(self, table_name):
        """
        This methods help us to add column to the table.
        """
        db.execute_cud_query(f"ALTER TABLE {table_name} ADD {self.col_name} {self.data_type}")
        
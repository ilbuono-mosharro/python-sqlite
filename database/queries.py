from core.settings import db

class Query:
    """
    Is a class to manage the queries.
    """
    def __init__(self):
        """
        This constructor takes no arguments, column and values are two list which 
        help us to keep track the column of the table and the value from the user input.
        """
        self.columns = []
        self.values = []

    def retrieve_columns(self):
        """
        This method retrive all the columns from the table 
        and check if not the column is id then append the column name to the columns list.
        """
        cols = db.execute_query_fetch("PRAGMA table_info(users)")
        for col in cols:
            if not col[1] == "id":
                self.columns.append(col[1])

    def add_values(self, value):
        """
        This method take a value argument from the user input and append to values list.
        """
        self.values.append(value)
    
    def add_record(self, table_name):
        """
        This method take no arguments and insert a record to the database, 
        we use join to convert the lists of the columns and the values to a single string.
        """
        col_to_string = ", ".join(self.columns)
        val_to_string = ", ".join(f"'{val}'" for val in self.values)
        db.execute_cud_query(f"INSERT INTO {table_name} ({col_to_string}) VALUES ({val_to_string})")
    
    def update_record(self, id):
        """
        This method take the id arguments from the user input and update a record from the database, 
        we use zip to merge the list columns and the list values, then we iterate and any value using join to add "=" 
        and append to list data then using join convert the list data to a single string.
        """
        data = []
        zip_col_val = zip(self.columns, self.values)
        conv_to_list = list(zip_col_val)
        for x in conv_to_list:
            data.append("=".join(x))
        data_to_str = ', '.join(data)
        db.execute_cud_query(f"UPDATE users SET {data_to_str} WHERE id={id}")

    def delete_record(self, table_name, id):
        """
        This method delete a record and take two argument id and the name of the table from the user input.
        """
        db.execute_cud_query(f"DELETE FROM {table_name} WHERE id={id}")
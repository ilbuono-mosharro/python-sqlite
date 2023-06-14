from database.tables import Tables
from database.columns import TablesColumn
from database.queries import Query, db

menu_list = [
    "1:Choose a table you want to work with", "2:Create a Table", "3:Delete a Table", "4:List the Tables", "5:Inspect a table",
    "6:Insert a new record", "7:Delete a record", "8:Update a record", "9:List the records", "10: Exit"
    ]

def menu():
    choices = "\n".join(menu_list)
    print(choices)
    return choices

def main():
    start = True
    while start:
        try:
            first_input = int(input("Choose an option from the list: "))
            if first_input == 1:
                db_name_input = input("Enter the name of the table: ")
                table = Tables()
                if db_name_input in table.all_tables:
                    query = Query()
                    query.retrieve_columns()
                    for col in query.columns:
                        value = input(f"Enter a value for the column {col}: ")
                        query.add_values(value)
                    query.add_record(db_name_input)
                    print("The record has been saved successfully.")
                else:
                    print(f"The Table {db_name_input} not found, please try again!")
                    menu()
            elif first_input == 2:
                table_name = input("Enter the name of the table?: ")
                Tables.create(table_name)
                number_columns = int(input("How many column want to create?: "))
                for num in range(number_columns):
                    column_name = input(f"Enter the name of the column?: ")
                    column_data_type = input(f"Enter the datatype of the column {column_name}?: ")
                    columns = TablesColumn(column_name, column_data_type)
                    columns.add_column(table_name)
                print("The columns has been saved successfully.")
            elif first_input == 3:
                table_name = input("Enter the name of the table?: ")
                table = Tables()
                if db_name_input in table.all_tables:
                    table.drop(table_name)
                    print("La tabella è stata cancellato con successo.")
                else:
                    print(f"The Table {db_name_input} not found, please try again!")
                    menu()
            elif first_input == 4:
                tables = Tables()
                tables.retrieve_tables()
                print("\n".join(tables.all_tables))
            elif first_input == 5:
                table_name = input("Enter the name of the table?: ")
                tables = Tables()
                if db_name_input in table.all_tables:
                    data = tables.get_table(table_name)
                    print(data)
                else:
                    print(f"The Table {db_name_input} not found, please try again!")
                    menu()
            elif first_input == 6:
                table_name = input("Enter the name of the table?: ")
                query = Query()
                query.retrieve_columns()
                for col in query.columns:
                    value = input(f"Enter a value for the colomn {col}: ")
                    query.add_values(value)
                query.add_record(table_name)
                print("The record has been saved successfully.")
            elif first_input == 7:
                table_name = input("Enter the name of the table?: ")
                query = Query()
                id = int(input("Enter the id of the record you want delete: "))
                query.delete_record(table_name, id)
                print("The record has been deleted successfully.")
            elif first_input == 8:
                table_name = input("Enter the name of the table?: ")
                id = int(input("Enter the id of the record you want uddate: "))
                query = Query()
                query.retrieve_columns()
                for col in query.columns:
                    value = input(f"Enter a value for the colomn {col}: ")
                    query.add_values(f"'{value}'")
                query.update_record(id)
                print("The record has been updae successfully.")
            elif first_input == 9:
                table_name = input("Enter the name of the table?: ")
                table = Tables()
                table.get_table(table_name)
            elif first_input == 10:
                start = False
            else:
                print("Enter a choice from a menu list")
                menu()
            db.disconnect()
        except ValueError:
            menu()


if __name__ == "__main__":
    main()

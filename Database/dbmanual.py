import sqlite3
from dbHelper import DBHelper


def main():
    # Initialize the DBHelper with the path to the database file
    db = DBHelper("genesis.db")
    
    
    table_name = "templates"
    columns = {
        "templateid": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "creator": "TEXT",
        "template": "TEXT NOT NULL UNIQUE",
        "assignedTo": "INTEGER"
    }
    
    db.create_table(table_name,columns)

    

if __name__ == "__main__":
    main()

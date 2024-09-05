import sqlite3

class DBHelper:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Create a new table with the given columns if it does not already exist.
        
        :param table_name: Name of the table to create.
        :param columns: Dictionary of column names and their types.
        """
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if self.cursor.fetchone() is None:
            columns_def = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
            self.cursor.execute(f"CREATE TABLE {table_name} ({columns_def})")
            self.conn.commit()

    def insert_value(self, table_name, values):
        """
        Insert a value into the specified table.
        
        :param table_name: Name of the table to insert into.
        :param values: Dictionary of column names and values to insert.
        """
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['?' for _ in values])
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", tuple(values.values()))
        self.conn.commit()

    def read_all_values(self, table_name):
        """
        Read all values from the specified table.
        
        :param table_name: Name of the table to read from.
        :return: List of tuples containing all rows.
        """
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()
    
    def list_tables(self):
        """
        List all tables in the database.
        
        :return: List of table names.
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [row[0] for row in self.cursor.fetchall()]
    
    def delete_table(self, table_name):
        """
        Delete a table by its name.
        
        :param table_name: Name of the table to delete.
        """
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
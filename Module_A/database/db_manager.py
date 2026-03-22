from database.table import Table

class DatabaseManager:
    def __init__(self):
        self.databases = {}  # Dictionary to store databases as {db_name: {table_name: Table instance}}

    def create_database(self, db_name):
        self.databases[db_name] = {}

    def delete_database(self, db_name):
        self.databases.pop(db_name, None)

    def list_databases(self):
        return list(self.databases.keys())

    def create_table(self, db_name, table_name, schema, order=8, search_key=None):
        table = Table(table_name, schema, order, search_key)
        self.databases[db_name][table_name] = table

    def delete_table(self, db_name, table_name):
        self.databases[db_name].pop(table_name, None)

    def list_tables(self, db_name):
        return list(self.databases[db_name].keys())

    def get_table(self, db_name, table_name):
        return self.databases[db_name][table_name]

from database.bplustree import BPlusTree

class Table:
    def __init__(self, name, schema, order=8, search_key=None):
        self.name = name                             # Name of the table
        self.schema = schema                         # Table schema: dict of {column_name: data_type}
        self.order = order                           # Order of the B+ Tree (max number of children)
        self.data = BPlusTree(order=order)           # Underlying B+ Tree to store the data
        self.search_key = search_key                 # Primary or search key used for indexing (must be in schema)

    def validate_record(self, record):
        for col in self.schema:
            if col not in record:
                raise ValueError(f"Missing column {col}")

    def insert(self, record):
        self.validate_record(record)
        key = record[self.search_key]
        self.data.insert(key, record)

    def get(self, record_id):
        return self.data.search(record_id)

    def get_all(self):
        return [v for _, v in self.data.get_all()]

    def update(self, record_id, new_record):
        self.data.update(record_id, new_record)

    def delete(self, record_id):
        self.data.delete(record_id)

    def range_query(self, start_value, end_value):
        return [v for _, v in self.data.range_query(start_value, end_value)]

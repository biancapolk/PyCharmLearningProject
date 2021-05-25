import sqlite3

# Internal representation that contain the properties of an item
class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Return JSON representation of the model
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM  items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        # if row exists, return JSON
        if row:
            return cls(*row)

    @classmethod
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()

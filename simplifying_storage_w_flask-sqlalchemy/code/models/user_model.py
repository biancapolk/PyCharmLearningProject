import sqlite3
from db import db


# Create user class - MODELS - internal representation
class UserModel:
    __tablename__ = 'users'

    id = db.column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # Finds user by username in the db
    @classmethod
    def find_by_username(cls, username):  # finds username
        connection = sqlite3.connect('data.db')  # setting up connection
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)  # query
        result = cursor.execute(query, (username,))  # running the query, has to be in the form of a tuple, hence the ,
        row = result.fetchone()  # gets the first row out of the results
        if row:
            user = cls(*row)  # passing row as a set of positional argument
        else:
            user = None  # returning a user object or NONE

        connection.close()
        return user

    # Finds user by username in the db
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

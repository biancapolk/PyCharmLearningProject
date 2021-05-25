import sqlite3
from flask_restful import Resource, reqparse


# Create user class
class User():
    TABLE_NAME = 'users'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # Finds user by username in the db
    @classmethod
    def find_by_username(cls, username):  # finds username
        connection = sqlite3.connect('data.db')  # setting up connection
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?"  # query
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


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201

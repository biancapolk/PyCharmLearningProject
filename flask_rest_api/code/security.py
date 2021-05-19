from werkzeug.security import safe_str_cmp
from user import User

# In-memory table of our registered users
# List of users that have key:value data assignments
users = [
    {
        'id': 1234,
        'username': 'Bia',
        'password': 'asdf'
    }
]

# Allows us to map a user by its username
username_mapping = {'Bia': {
        'id': 1234,
        'username': 'Bia',
        'password': "asdf"
    }
}

# Allows us to map a user by its user_id
userid_mapping = { 1234 :
    {
        'id': 1234,
        'username': 'Bia',
        'password': "asdf"
    }
}

# userid_mapping{}
# given a username or password selects users from our list
def authenticate(self,username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

# Q here...
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)




# users = [
#     User(1, 'user1', 'abcxyz'),
#     User(2, 'user2', 'abcxyz'),
# ]

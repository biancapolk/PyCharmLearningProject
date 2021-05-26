from user import User

# In-memory table of our registered users
# List of users that have key:value data assignments
users = [
    User(1234, 'Bia', 'asdf')
]

# Allows us to map a user by its username
username_mapping = {u.username: u for u in users}
# Allows us to map a user by its user_id
userid_mapping = {u.id: u for u in users}


# userid_mapping{}
# given a username or password selects users from our list
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


# Q here...
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)


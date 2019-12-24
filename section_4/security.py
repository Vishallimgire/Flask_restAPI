from werkzeug.security import safe_str_cmp
from user import User
print(__name__)

users = [
    User(1, 'vishal', 'asdf')
]

username_mapping = { u.username: u for u in users}
print(username_mapping)

userid_mapping = { u.id: u for u in users }
print(userid_mapping)

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    print('payload', payload)
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
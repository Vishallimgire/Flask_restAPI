import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        return  
    @classmethod
    def find_by_userid(cls, user_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM users where id=?'
        result = cursor.execute(query,(user_id,)).fetchone()
        user = cls(*result) if result else None
        connection.close()
        print('userid user', user)
        return user

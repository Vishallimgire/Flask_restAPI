import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'
cursor.execute(create_table)

insert_query = 'INSERT INTO users VALUES(?, ?, ?)'
users = [
    (1, 'vishal', 'limgire'),
    (2, 'allen', 'kedari')
]
cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM users'
for user in cursor.execute(select_query):
    print(user)

connection.commit()
connection.close()
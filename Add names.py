import sqlite3

conn = sqlite3.connect('usernames.db')
c = conn.cursor()

usernames = ['username1', 'username2']#here

for username in usernames:
    c.execute("INSERT INTO usernames VALUES (?)", (username,))

conn.commit()
conn.close()

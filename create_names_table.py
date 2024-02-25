import sqlite3

conn = sqlite3.connect('usernames.db')

c = conn.cursor()

c.execute('''CREATE TABLE usernames
             (username text)''')

conn.commit()

conn.close()

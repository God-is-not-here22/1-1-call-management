import sqlite3

conn = sqlite3.connect('names.db')

c = conn.cursor()

c.execute('''CREATE TABLE names
             (name text)''')

conn.commit()

conn.close()

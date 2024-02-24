import sqlite3

conn = sqlite3.connect('usernames.db')

c = conn.cursor()

c.execute('''CREATE TABLE pairs
             (pair1 text, pair2 text)''')

conn.commit()

conn.close()

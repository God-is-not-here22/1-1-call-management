import sqlite3

conn = sqlite3.connect('usernames.db')
c = conn.cursor()

names_to_delete = ['Parvati Jain', 'John Doe', 'Jane Doe']

for name in names_to_delete:
    c.execute("DELETE FROM usernames WHERE username = ?", (name,))

conn.commit()
conn.close()


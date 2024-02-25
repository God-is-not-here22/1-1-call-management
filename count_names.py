import sqlite3

conn = sqlite3.connect('usernames.db')
c = conn.cursor()

c.execute("SELECT username FROM usernames")
rows = c.fetchall()

print(f'There are {len(rows)} rows in the table.')

for row in rows:
    print(row[0])

conn.close()

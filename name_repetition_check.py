import sqlite3

conn = sqlite3.connect('usernames.db')
c = conn.cursor()

c.execute("SELECT username, COUNT(username) FROM usernames GROUP BY username HAVING COUNT(username) > 1")
rows = c.fetchall()

if rows:
    print("The following names are duplicated:")
    for row in rows:
        print(f"{row[0]} appears {row[1]} times")
else:
    print("There are no duplicate usernames in the table.")

conn.close()

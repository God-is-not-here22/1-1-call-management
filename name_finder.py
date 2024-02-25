import sqlite3

conn = sqlite3.connect('usernames.db')
c = conn.cursor()

names_to_check = ['Echo', 'Alpha', 'Bravo']#here

for name in names_to_check:
    c.execute("SELECT username FROM usernames WHERE username = ?", (name,))
    row = c.fetchone()

    if row is None:
        print(f"The username {name} is not in the table.")
    else:
        print(f"The username {name} is in the table.")

conn.close()

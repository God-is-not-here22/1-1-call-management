import sqlite3

def add_pairings(pairings):
    conn = sqlite3.connect('usernames.db')
    c = conn.cursor()

    for pair in pairings:
        c.execute("INSERT INTO pairs (pair1, pair2) VALUES (?, ?)", (pair[0], pair[1]))
        print(f'Pairing @{pair[0]} <-> @{pair[1]} has been added to the database.')

    conn.commit()
    conn.close()

add_pairings([('username1', 'username2'), ('username3', 'username4')])#here

import sqlite3

def print_pairings():
    conn = sqlite3.connect('usernames.db')
    c = conn.cursor()

    c.execute("SELECT * FROM pairs")

    pairings = c.fetchall()

    for pair in pairings:
        print(f'Pairing @{pair[0]} <-> @{pair[1]}')

    conn.close()

print_pairings()

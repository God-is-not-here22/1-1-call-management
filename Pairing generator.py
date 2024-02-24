import sqlite3
import random

conn = sqlite3.connect('usernames.db')
c = conn.cursor()

c.execute("SELECT username FROM usernames")
usernames = [row[0] for row in c.fetchall()]

if len(usernames) % 2 != 0:
    usernames.append('username1')#here

def get_pairing():
    random.shuffle(usernames)
    pairings = list(zip(usernames[::2], usernames[1::2]))
    return pairings

def valid_pairing(pairing):
    c.execute("SELECT * FROM pairs WHERE pair1 = ? AND pair2 = ?", pairing)
    return c.fetchone() is None

def valid_pairing_unordered(p):
    return valid_pairing(p) and valid_pairing((p[1], p[0]))

total_pairings = len(usernames) * (len(usernames) - 1) // 2

c.execute("SELECT COUNT(*) FROM pairs")
num_records = c.fetchone()[0]

if num_records >= total_pairings:
    print("All possible pairings have been used.")
    conn.close()
else:
    pairings = get_pairing()
    while not all(valid_pairing_unordered(p) for p in pairings):
        pairings = get_pairing()

    for pair in pairings:
        c.execute("INSERT INTO pairs (pair1, pair2) VALUES (?, ?)", pair)

    conn.commit()
    conn.close()

    print('New pairings! :people_with_bunny_ears_partying:\n')
    for p1, p2 in pairings:
        print(f'@{p1} <-> @{p2}')

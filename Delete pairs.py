import sqlite3

def delete_pairings(pairs):
    conn = sqlite3.connect('usernames.db')
    c = conn.cursor()

    for pair in pairs:
        pair1, pair2 = pair

        c.execute("SELECT * FROM pairs WHERE (pair1 = ? AND pair2 = ?) OR (pair1 = ? AND pair2 = ?)", (pair1, pair2, pair2, pair1))

        pair = c.fetchone()

        if pair is None:
            print(f'Pairing @{pair1} <-> @{pair2} does not exist in the database.')
            continue

        c.execute("DELETE FROM pairs WHERE (pair1 = ? AND pair2 = ?) OR (pair1 = ? AND pair2 = ?)", (pair1, pair2, pair2, pair1))

        print(f'Pairing @{pair1} <-> @{pair2} has been deleted from the database.')

    conn.commit()
    conn.close()

pairs_to_delete = [('username1', 'username2'), ('username3', 'username4')]#here
delete_pairings(pairs_to_delete)

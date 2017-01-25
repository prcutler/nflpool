import sqlite3

conn = sqlite3.connect('nflpool.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Player;

CREATE TABLE Picks (
    firstname    TEXT NOT NULL,
    lastname    TEXT NOT NULL,
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    season TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    timestamp TEXT NOT NULL
    key
    afc_east_first TEXT NOT NULL
    afc_east_second TEXT NOT NULL
    afc_east_last TEXT NOT NULL
    afc_north_first TEXT NOT NULL
    afc_north_second TEXT NOT NULL
    afc_north_last TEXT NOT NULL
    afc_south_first TEXT NOT NULL
    afc_south_second TEXT NOT NULL
    afc_south_last TEXT NOT NULL
    afc_west_first TEXT NOT NULL
    afc_west_second TEXT NOT NULL
    afc_west_last TEXT NOT NULL
    nfc_east_first TEXT NOT NULL
    nfc_east_second TEXT NOT NULL
    nfc_east_last TEXT NOT NULL
    nfc_north_first TEXT NOT NULL
    nfc_north_second TEXT NOT NULL
    nfc_north_last TEXT NOT NULL
    nfc_south_first TEXT NOT NULL
    nfc_south_second TEXT NOT NULL
    nfc_south_last TEXT NOT NULL
    nfc_west_first TEXT NOT NULL
    nfc_west_second TEXT NOT NULL
    nfc_west_last TEXT NOT NULL
    afc_wildcard1 TEXT NOT NULL
    afc_wildcard2 TEXT NOT NULL
    nfc_wildcard1 TEXT NOT NULL
    nfc_wildcard2 TEXT NOT NULL
    afc_rushing_leader TEXT NOT NULL
    afc_passing_leader TEXT NOT NULL
    afc_receiving_leader TEXT NOT NULL
    afc_sacks_leader TEXT NOT NULL
    afc_int_leader TEXT NOT NULL
    nfc_rushing_leader TEXT NOT NULL
    nfc_passing_leader TEXT NOT NULL
    nfc_receiving_leader TEXT NOT NULL
    nfc_sacks_leader TEXT NOT NULL
    nfc_int_leader TEXT NOT NULL
    afc_pf TEXT NOT NULL
    nfc_pf TEXT NOT NULL
    tiebreaker TEXT NOT NULL

)
''')
conn.commit()
conn.close()

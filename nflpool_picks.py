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
    afc_rushing_first TEXT NOT NULL
    afc_rushing_second TEXT NOT NULL
    afc_rushing_third TEXT NOT NULL
    afc_passing_first TEXT NOT NULL
    afc_passing_second TEXT NOT NULL
    afc_passing_third TEXT NOT NULL
    afc_receiving_first TEXT NOT NULL
    afc_receiving_second TEXT NOT NULL
    afc_receiving_third TEXT NOT NULL
    afc_sacks_first TEXT NOT NULL
    afc_sacks_second TEXT NOT NULL
    afc_sacks_third TEXT NOT NULL
    afc_int_first TEXT NOT NULL
    afc_int_second TEXT NOT NULL
    afc_int_third TEXT NOT NULL
    nfc_rushing_first TEXT NOT NULL
    nfc_rushing_second TEXT NOT NULL
    nfc_rushing_third TEXT NOT NULL
    nfc_passing_first TEXT NOT NULL
    nfc_passing_second TEXT NOT NULL
    nfc_passing_third TEXT NOT NULL
    nfc_receiving_first TEXT NOT NULL
    nfc_receiving_second TEXT NOT NULL
    nfc_receiving_third TEXT NOT NULL
    nfc_sacks_first TEXT NOT NULL
    nfc_sacks_second TEXT NOT NULL
    nfc_sacks_third TEXT NOT NULL
    nfc_int_first TEXT NOT NULL
    nfc_int_second TEXT NOT NULL
    nfc_int_third TEXT NOT NULL
    afc_pf TEXT NOT NULL
    nfc_pf TEXT NOT NULL
    specialteams_td TEXT NOT NULL

)
''')
conn.commit()
conn.close()

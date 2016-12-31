import sqlite3
import json

# This file creates the table in the database to store each player's picks for every category in NFLPool.

conn = sqlite3.connect('nflpool.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS picks;

CREATE TABLE picks (
    firstname    TEXT NOT NULL,
    lastname    TEXT NOT NULL,
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    season TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    timestamp TEXT NOT NULL,
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    afc_east_first_pick TEXT NOT NULL,
    afc_east_second_pick TEXT NOT NULL,
    afc_east_last_pick TEXT NOT NULL,
    afc_north_first_pick TEXT NOT NULL,
    afc_north_second_pick TEXT NOT NULL,
    afc_north_last_pick TEXT NOT NULL,
    afc_south_first_pick TEXT NOT NULL,
    afc_south_second_pick TEXT NOT NULL,
    afc_south_last_pick TEXT NOT NULL,
    afc_west_first_pick TEXT NOT NULL,
    afc_west_second_pick TEXT NOT NULL,
    afc_west_last_pick TEXT NOT NULL,
    nfc_east_first_pick TEXT NOT NULL,
    nfc_east_second_pick TEXT NOT NULL,
    nfc_east_last_pick TEXT NOT NULL,
    nfc_north_first_pick TEXT NOT NULL,
    nfc_north_second_pick TEXT NOT NULL,
    nfc_north_last_pick TEXT NOT NULL,
    nfc_south_first_pick TEXT NOT NULL,
    nfc_south_second_pick TEXT NOT NULL,
    nfc_south_last_pick TEXT NOT NULL,
    nfc_west_first_pick TEXT NOT NULL,
    nfc_west_second_pick TEXT NOT NULL,
    nfc_west_last_pick TEXT NOT NULL,
    afc_wildcard1_pick TEXT NOT NULL,
    afc_wildcard2_pick TEXT NOT NULL,
    nfc_wildcard1_pick TEXT NOT NULL,
    nfc_wildcard2_pick TEXT NOT NULL,
    afc_rushing_leader_pick TEXT NOT NULL,
    afc_passing_leader_pick TEXT NOT NULL,
    afc_receiving_leader_pick TEXT NOT NULL,
    afc_sacks_leader_pick TEXT NOT NULL,
    afc_int_leader_pick TEXT NOT NULL,
    nfc_rushing_leader_pick TEXT NOT NULL,
    nfc_passing_leader_pick TEXT NOT NULL,
    nfc_receiving_leader_pick TEXT NOT NULL,
    nfc_sacks_leader_pick TEXT NOT NULL,
    nfc_int_leader_pick TEXT NOT NULL,
    afc_pf_pick TEXT NOT NULL,
    nfc_pf_pick TEXT NOT NULL,
    tiebreaker_pick TEXT NOT NULL


)

''')
conn.commit()
conn.close()

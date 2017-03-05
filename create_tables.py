import sqlite3
import json
import requests
import secret
from requests.auth import HTTPBasicAuth
import csv


def main():
    create_teams_table()
    create_division_standings_table()
    create_conference_teams_table()
    create_playoff_rankings_table()
    populate_team_info()
    create_player_picks()
    create_nflplayers_table()
    populate_nflplayers_table()
#    add_player_picks()


# Create the teams table with team name, id, city, etc
def create_teams_table():
    conn = sqlite3.connect('nflpool.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS teams;

    CREATE TABLE teams (
        name    TEXT NOT NULL UNIQUE,
        team_id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
        city    TEXT NOT NULL,
        abbreviation  TEXT,
        conference  TEXT,
        division  TEXT
    )

    ''')
    conn.commit()
    conn.close()


# Create the Division Standings Table
def create_division_standings_table():
    conn = sqlite3.connect('nflpool.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS division_standings;

    CREATE TABLE division_standings (
        week    TEXT NOT NULL,
        season INTEGER NOT NULL,
        timestamp INTEGER NOT NULL,
        rank INTEGER NOT NULL,
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id  INTEGER NOT NULL UNIQUE

    )

    ''')
    conn.commit()
    conn.close()


# Create the Conference Points For table
def create_conference_teams_table():
    conn = sqlite3.connect('nflpool.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS conference_standings;

    CREATE TABLE conference_standings (
        week    TEXT NOT NULL,
        season INTEGER NOT NULL,
        timestamp INTEGER NOT NULL,
        rank  INTEGER NOT NULL,
        points_for INTEGER NOT NULL,
        team_id  INTEGER NOT NULL UNIQUE,
        pr_td INTEGER NOT NULL,
        kr_td INTEGER NOT NULL,
        key    INTEGER PRIMARY KEY AUTOINCREMENT

    )

    ''')
    conn.commit()
    conn.close()


# Create table for playoff rankings

def create_playoff_rankings_table():
    conn = sqlite3.connect('nflpool.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS playoff_rankings;

    CREATE TABLE playoff_rankings (
        week    TEXT NOT NULL,
        season INTEGER NOT NULL,
        timestamp INTEGER NOT NULL,
        rank  INTEGER NOT NULL,
        team_id  INTEGER NOT NULL UNIQUE,
        key    INTEGER PRIMARY KEY AUTOINCREMENT

    )

    ''')
    conn.commit()
    conn.close()


def populate_team_info():
    x = 0
    y = 0

    response = requests.get(
    'https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/conference_team_standings.json',
    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    data = response.json()

    #       This code shows it's a list with 16 items - each team!
    teamlist = data["conferenceteamstandings"]["conference"][0]["teamentry"]
    #        print(len(teamlist))
    #        print(type(teamlist))

    # Create a loop to extract each team name (AFC first, then NFC)

    for afc_team_list in teamlist:
        afc_team_name = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Name"]
        afc_team_city = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["City"]
        afc_team_id = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"]
        afc_team_abbr = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Abbreviation"]
        #            print((afc_team_name), (afc_team_city), (afc_team_id), (afc_team_abbr))
        x = x + 1

        conn = sqlite3.connect('nflpool.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO teams(name, team_id, city, abbreviation, conference)
                    VALUES(?,?,?,?, "AFC")''', (afc_team_name, afc_team_id, afc_team_city, afc_team_abbr))

        conn.commit()
        conn.close()

    for nfc_team_list in teamlist:
        nfc_team_name = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Name"]
        nfc_team_city = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["City"]
        nfc_team_id = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["ID"]
        nfc_team_abbr = data["conferenceteamstandings"]["conference"][1]["teamentry"][y]["team"]["Abbreviation"]
        #            print((nfc_team_name), (nfc_team_city), (nfc_team_id), (nfc_team_abbr))
        y = y + 1

        conn = sqlite3.connect('nflpool.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT OR IGNORE INTO teams(name, team_id, city, abbreviation, conference)
                    VALUES(?,?,?,?, "NFC")''', (nfc_team_name, nfc_team_id, nfc_team_city, nfc_team_abbr))

        # INSERT DIVISION NAMES INTO DATABASE MANUALLY
        cur.execute('''UPDATE teams SET division = "EAST" WHERE team_id IN (48,49,50,51,52,53,54,55)''')
        cur.execute('''UPDATE teams SET division = "NORTH" WHERE team_id IN (56,57,58,59,60,61,62,63)''')
        cur.execute('''UPDATE teams SET division = "SOUTH" WHERE team_id IN (64,65,66,67,68,69,70,71)''')
        cur.execute('''UPDATE teams SET division = "WEST" WHERE team_id IN (72,73,74,75,76,77,78,79,80)''')

        conn.commit()
        conn.close()


# Create table for each player's picks
def create_player_picks():
    conn = sqlite3.connect('nflpool.sqlite')
    cur = conn.cursor()

    # Do some setup
    cur.executescript('''
    DROP TABLE IF EXISTS player_picks;

    CREATE TABLE player_picks (
        timestamp TEXT NOT NULL,
        season TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        firstname    TEXT NOT NULL,
        lastname    TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
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


def create_nflplayers_table():
    conn = sqlite3.connect('nflpool.sqlite')
    cur = conn.cursor()

    # Do some setup
    cur.executescript('''
    DROP TABLE IF EXISTS nflplayers;

    CREATE TABLE nflplayers (
        firstname    TEXT NOT NULL,
        lastname    TEXT NOT NULL,
        player_id  INTEGER NOT NULL,
        key  INTEGER PRIMARY KEY AUTOINCREMENT,
        season INTEGER NOT NULL,
        team_id INTEGER,
        position  TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def populate_nflplayers_table():
    response = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/active_players.json',
    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    player_info = response.json()
    player_list = player_info["activeplayers"]["playerentry"]
   # print (player_list[0]["team"]["City"])

    for players in player_list:
        try:
                firstname = (players["player"]["FirstName"])
                lastname = (players["player"]["LastName"])
                player_id = (players["player"]["ID"])
                team_id = (players["team"]["ID"])
                position = (players["player"]["Position"])
        except KeyError:
                continue
#        print (firstname, lastname, player_id, team_id, position)


        conn = sqlite3.connect('nflpool.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO nflplayers(firstname, lastname, player_id, team_id, position, season)
            VALUES(?,?,?,?, ?, "2016")''', (firstname, lastname, player_id, team_id, position))

        conn.commit()
        conn.close()


def add_player_picks():
    conn = sqlite3.connect('nflpool.sqlite')
    cur = conn.cursor()

    with open('data/2016_playerpicks.csv', 'rb') as reader:
        for timestamp, \
                season, \
                user_id, \
                firstname, \
                lastname, \
                email, \
                afc_east_first_pick, \
                afc_east_second_pick, \
                afc_east_last_pick, \
                afc_north_first_pick, \
                afc_north_second_pick, \
                afc_north_last_pick, \
                afc_south_first_pick, \
                afc_south_second_pick, \
                afc_south_last_pick, \
                afc_west_first_pick, \
                afc_west_second_pick, \
                afc_west_last_pick, \
                nfc_east_first_pick, \
                nfc_east_second_pick, \
                nfc_east_last_pick, \
                nfc_north_first_pick, \
                nfc_north_second, \
                nfc_north_last_pick, \
                nfc_south_first_pick, \
                nfc_south_second_pick, \
                nfc_south_last_pick, \
                nfc_west_first_pick, \
                nfc_west_second_pick, \
                nfc_west_last_pick, \
                afc_wildcard1_pick, \
                afc_wildcard2_pick, \
                nfc_wildcard1_pick, \
                nfc_wildcard2_pick, \
                afc_rushing_leader_pick, \
                afc_passing_leader_pick, \
                afc_receiving_leader_pick, \
                afc_sacks_leader_pick, \
                afc_int_leader_pick, \
                afc_pf_pick, \
                nfc_rushing_leader_pick, \
                nfc_passing_leader_pick, \
                nfc_receiving_leader_pick, \
                nfc_sacks_leader_pick, \
                nfc_int_leader_pick, \
                nfc_pf_pick, \
                tiebreaker_pick \
                in reader:
            cur.execute('''INSERT OR IGNORE INTO player_picks (
                timestamp,
                season,
                user_id,
                firstname,
                lastname,
                email,
                afc_east_first_pick,
                afc_east_second_pick,
                afc_east_last_pick,
                afc_north_first_pick,
                afc_north_second_pick,
                afc_north_last_pick,
                afc_south_first_pick,
                afc_south_second_pick,
                afc_south_last_pick,
                afc_west_first_pick,
                afc_west_second_pick,
                afc_west_last_pick,
                nfc_east_first_pick,
                nfc_east_second_pick,
                nfc_east_last_pick,
                nfc_north_first_pick,
                nfc_north_second_pick,
                nfc_north_last_pick,
                nfc_south_first_pick,
                nfc_south_second_pick,
                nfc_south_last_pick,
                nfc_west_first_pick,
                nfc_west_second_pick,
                nfc_west_last_pick,
                afc_wildcard1_pick,
                afc_wildcard2_pick,
                nfc_wildcard1_pick,
                nfc_wildcard2_pick,
                afc_rushing_leader_pick,
                afc_passing_leader_pick,
                afc_receiving_leader_pick,
                afc_sacks_leader_pick,
                afc_int_leader,
                afc_pf_pick,
                nfc_rushing_leader_pick,
                nfc_passing_leader_pick,
                nfc_receiving_leader_pick,
                nfc_sacks_leader_pick,
                nfc_int_leader_pick,
                nfc_pf_pick,
                tiebreaker_pick
                        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', \
 \
                        (timestamp, \
                        season, \
                        user_id, \
                        firstname, \
                        lastname, \
                        email, \
                        afc_east_first_pick, \
                        afc_east_second_pick, \
                        afc_east_last_pick, \
                        afc_north_first_pick, \
                        afc_north_second_pick, \
                        afc_north_last_pick, \
                        afc_south_first_pick, \
                        afc_south_second_pick, \
                        afc_south_last_pick, \
                        afc_west_first_pick, \
                        afc_west_second_pick, \
                        afc_west_last_pick, \
                        nfc_east_first_pick, \
                        nfc_east_second_pick, \
                        nfc_east_last_pick, \
                        nfc_north_first_pick, \
                        nfc_north_second_pick, \
                        nfc_north_last_pick, \
                        nfc_south_first_pick, \
                        nfc_south_second_pick, \
                        nfc_south_last_pick, \
                        nfc_west_first_pick, \
                        nfc_west_second_pick, \
                        nfc_west_last_pick, \
                        afc_wildcard1_pick, \
                        afc_wildcard2_pick, \
                        nfc_wildcard1_pick, \
                        nfc_wildcard2_pick, \
                        afc_rushing_leader_pick, \
                        afc_passing_leader_pick, \
                        afc_receiving_leader_pick, \
                        afc_sacks_leader_pick, \
                        afc_int_leader, \
                        afc_pf_pick, \
                        nfc_rushing_leader_pick, \
                        nfc_passing_leader_pick, \
                        nfc_receiving_leader_pick, \
                        nfc_sacks_leader_pick, \
                        nfc_int_leader_pick, \
                        nfc_pf_pick, \
                        tiebreaker_pick))

    conn.commit()
    conn.close()



# TODO Create table for player statistics

if __name__ == '__main__':
    main()

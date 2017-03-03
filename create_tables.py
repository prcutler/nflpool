import sqlite3
import json


def main():
    create_teams_table()
    create_division_standings_table()
    create_conference_teams_table()
    create_playoff_rankings_table()
    populate_team_info()
    create_player_picks()
    create_nflplayers_table()


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
        id    INTEGER PRIMARY KEY AUTOINCREMENT

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
        id    INTEGER PRIMARY KEY AUTOINCREMENT

    )

    ''')
    conn.commit()
    conn.close()


def populate_team_info():
    # Change the name of the file to open to match the query below:
    x = 0
    y = 0

    with open('data/20160920-conference-team-standings.json') as file:
        alltext = file.readlines()  # Put each line into a list

    for lines in alltext:
        if lines.startswith('{'):
            rawdata = lines
            data = json.loads(rawdata)

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
        firstname    TEXT NOT NULL,
        lastname    TEXT NOT NULL,
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        season TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        timestamp TEXT NOT NULL,
        afc_east_first TEXT NOT NULL,
        afc_east_second TEXT NOT NULL,
        afc_east_last TEXT NOT NULL,
        afc_north_first TEXT NOT NULL,
        afc_north_second TEXT NOT NULL,
        afc_north_last TEXT NOT NULL,
        afc_south_first TEXT NOT NULL,
        afc_south_second TEXT NOT NULL,
        afc_south_last TEXT NOT NULL,
        afc_west_first TEXT NOT NULL,
        afc_west_second TEXT NOT NULL,
        afc_west_last TEXT NOT NULL,
        nfc_east_first TEXT NOT NULL,
        nfc_east_second TEXT NOT NULL,
        nfc_east_last TEXT NOT NULL,
        nfc_north_first TEXT NOT NULL,
        nfc_north_second TEXT NOT NULL,
        nfc_north_last TEXT NOT NULL,
        nfc_south_first TEXT NOT NULL,
        nfc_south_second TEXT NOT NULL,
        nfc_south_last TEXT NOT NULL,
        nfc_west_first TEXT NOT NULL,
        nfc_west_second TEXT NOT NULL,
        nfc_west_last TEXT NOT NULL,
        afc_wildcard1 TEXT NOT NULL,
        afc_wildcard2 TEXT NOT NULL,
        nfc_wildcard1 TEXT NOT NULL,
        nfc_wildcard2 TEXT NOT NULL,
        afc_rushing_leader TEXT NOT NULL,
        afc_passing_leader TEXT NOT NULL,
        afc_receiving_leader TEXT NOT NULL,
        afc_sacks_leader TEXT NOT NULL,
        afc_int_leader TEXT NOT NULL,
        nfc_rushing_leader TEXT NOT NULL,
        nfc_passing_leader TEXT NOT NULL,
        nfc_receiving_leader TEXT NOT NULL,
        nfc_sacks_leader TEXT NOT NULL,
        nfc_int_leader TEXT NOT NULL,
        afc_pf TEXT NOT NULL,
        nfc_pf TEXT NOT NULL,
        tiebreaker TEXT NOT NULL

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
        id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
        team INTEGER,
        position  TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# TODO Create table for player statistics

if __name__ == '__main__':
    main()

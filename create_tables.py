import sqlite3
import json

conn = sqlite3.connect('nflpool.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Teams;

CREATE TABLE Teams (
    name    TEXT NOT NULL UNIQUE,
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    city    TEXT NOT NULL,
    abbreviation  TEXT,
    conference  TEXT,
    division  TEXT
)

''')
conn.commit()
conn.close()

x = 0
y = 0

#Change the name of the file to open to match the query below:
with open('json/20160921-conference-team-standings.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)



#       This code shows it's a list with 16 items - each team!
        teamlist = data["conferenceteamstandings"]["conference"][0]["teamentry"]
#        print(len(teamlist))
#        print(type(teamlist))

        #Create a loop to extract each team name (AFC first, then NFC)

        for afc_team_list in teamlist:
            afc_team_name = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Name"]
            afc_team_city = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["City"]
            afc_team_id = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"]
            afc_team_abbr = data["conferenceteamstandings"]["conference"][0]["teamentry"][x]["team"]["Abbreviation"]
#            print((afc_team_name), (afc_team_city), (afc_team_id), (afc_team_abbr))
            x = x + 1

            conn = sqlite3.connect('nflpool.sqlite')
            cur = conn.cursor()

            cur.execute('''INSERT INTO Teams(name, id, city, abbreviation)
                        VALUES(?,?,?,?)''', (afc_team_name, afc_team_id, afc_team_city, afc_team_abbr))

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

            cur.execute('''INSERT OR IGNORE INTO Teams(name, id, city, abbreviation)
                        VALUES(?,?,?,?)''', (nfc_team_name, nfc_team_id, nfc_team_city, nfc_team_abbr))

            conn.commit()
            conn.close()




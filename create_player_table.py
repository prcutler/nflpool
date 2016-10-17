import sqlite3
import json

conn = sqlite3.connect('nflpool.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Player;

CREATE TABLE Player (
    firstname    TEXT NOT NULL,
    lastname    TEXT NOT NULL,
    id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
    team INTEGER,
    position  TEXT NOT NULL
)
''')
conn.commit()
conn.close()

x = 0
y = 0

#Change the name of the file to open to match the query below:
with open('json/20160921-cumulative-player-stats.json') as file:
    alltext = file.readlines()  #Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

#       Get a list of all players
        playerlist = data["cumulativeplayerstats"]["playerstatsentry"]
#        print(len(playerlist))
#        print(type(playerlist))

        for player in playerlist:
            player = data["cumulativeplayerstats"]["playerstatsentry"][x]["player"]
            firstname = player["FirstName"]
            lastname = player["LastName"]
            id = player["ID"]
            position = player["Position"]
            team = data["cumulativeplayerstats"]["playerstatsentry"][x]["team"]["ID"]
            print(firstname, lastname, id, team)


            conn = sqlite3.connect('nflpool.sqlite')
            cur = conn.cursor()

            cur.execute('''INSERT INTO Player(firstname, lastname, id, team, position)
                        VALUES(?,?,?,?,? )''', (firstname, lastname, id, team, position))

            conn.commit()
            conn.close()


            x = x + 1
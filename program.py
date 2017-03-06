import json
import csv
import requests
import sqlite3
from requests.auth import HTTPBasicAuth
import secret

base_url = 'https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/'


def main():
    division_standings()
    playoff_standings()
    playoff_standings()
    player_stats()
    points_for()
    tiebreaker()
    player_score()



# Get Division Standings for each team
def division_standings():
    pass


# Get Playoff Standings for each team (need number 5 & 6 in each conference)
def playoff_standings():
    pass


# Get individual statistics for each category
def player_stats():
    url = base_url + 'cumulative_player_stats.json?playerstats=Yds,Sacks,Int'
    response = requests.get((url),
    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    all_stats = response.json()
    stats = all_stats["cumulativeplayerstats"]["playerstatsentry"]

    for data in stats:
        try:
            player_id = (data["player"]["ID"])
            passyds = (data["stats"]["PassYards"]["#text"])
            rushyds = (data["stats"]["RushYards"]["#text"])
            recyds = (data["stats"]["RecYards"]["#text"])
            sacks = (data["stats"]["Sacks"]["#text"])
            interceptions = (data["stats"]["Interceptions"]["#text"])
#            print (player_id, passyds, rushyds, recyds, sacks, interceptions)
        except KeyError:
            continue

        conn = sqlite3.connect('nflpool.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT INTO player_stats(player_id, passyds, rushyds, recyds, sacks, interceptions, season)
            VALUES(?,?,?,?, ?, ?, "2016")''', (player_id, passyds, rushyds, recyds, sacks, interceptions))

        conn.commit()
        conn.close()


# Get points for for the number one team in each conference:
def points_for():
    pass


# Get the tiebreaker information
def tiebreaker():
    pass


# Calculate the player scores
def player_score():
    pass


if __name__ == '__main__':
    main()

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
    player_stats()
    conference_stats()
    division_score()
    ind_leaders_score()
    tiebreaker_pf_score()



# Get Division Standings for each team
def division_standings():
    url = base_url + 'division_team_standings.json'
    response = requests.get((url),
                            auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    data = response.json()

    for division in data['divisionteamstandings']['division']:
        for team in division['teamentry']:
            team_id = team['team']['ID']
            rank = team['rank']

            conn = sqlite3.connect('nflpool.sqlite')
            cur = conn.cursor()

            cur.execute('''INSERT INTO division_standings(team_id, rank)
                VALUES(?,?)''', (team_id, rank))

            conn.commit()
            conn.close()


# Get Playoff Standings for each team (need number 5 & 6 in each conference for Wild Card picks)
def playoff_standings():
    url = base_url + 'playoff_team_standings.json'
    response = requests.get((url),
                            auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    data = response.json()

    for conference in data['playoffteamstandings']['conference']:
        for team in conference['teamentry']:
            team_id = team['team']['ID']
            rank = team['rank']

            conn = sqlite3.connect('nflpool.sqlite')
            cur = conn.cursor()

            cur.execute('''INSERT INTO playoff_rankings(team_id, rank)
                VALUES(?,?)''', (team_id, rank))

            conn.commit()
            conn.close()


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


# Get conference stats - points_for, rank, and tiebreaker information
# TODO look into adding pr_td and kr_td instead of capturing individually

def conference_stats():
    url = base_url + 'conference_team_standings.json'
    response = requests.get((url),
                            auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

    data = response.json()

    for conference in data['conferenceteamstandings']['conference']:
        for team in conference['teamentry']:
            team_id = team['team']['ID']
            rank = team['rank']
            points_for = team['stats']['PointsFor']['#text']
            pr_td = team['stats']['PrTD']['#text']
            kr_td = team['stats']['KrTD']['#text']

            conn = sqlite3.connect('nflpool.sqlite')
            cur = conn.cursor()

            cur.execute('''INSERT INTO conference_standings(team_id, rank, points_for, pr_td, kr_td)
                VALUES(?,?,?,?,?)''', (team_id, rank, points_for, pr_td, kr_td,))

            conn.commit()
            conn.close()


# Calculate the player scores
def division_score():
    pass


def ind_leaders_score():
    pass


def tiebreaker_pf_score():
    pass


if __name__ == '__main__':
    main()

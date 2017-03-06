import json
import csv
import requests
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

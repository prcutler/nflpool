import requests
from bson import json_util
from requests.auth import HTTPBasicAuth
from pymongo import MongoClient
import json
import secret

# What year to pull data for
year = 2016

# Pull all active players and put in the collection of year value above
active_players = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/active_players.json',
                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

data = active_players.json()

client = MongoClient('localhost', 27017)
db = client.nflpooldb
collection = db[year]
collection.insert(data)

# Pull conference standings and put in the collection of year value above
conference_standings = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular/'
                                    'conference_team_standings.json',
                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

conference = conference_standings.json()

client = MongoClient('localhost', 27017)
db = client.nflpooldb
collection = db[year]
collection.insert(conference)

# Pull overall Team Standings needed for KrTD and PrTD
tiebreaker_data = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular'
                               '/overall_team_standings.json?teamstats=Kickoff%20Returns.TD,Punt%20Returns.TD',
                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

tiebreaker = tiebreaker_data.json()

client = MongoClient('localhost', 27017)
db = client.nflpooldb
collection = db[year]
collection.insert(tiebreaker)

# Pull overall Team Standings needed for KrTD and PrTD
tiebreaker_data = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular'
                               '/overall_team_standings.json?teamstats=Kickoff%20Returns.TD,Punt%20Returns.TD',
                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

tiebreaker = tiebreaker_data.json()

client = MongoClient('localhost', 27017)
db = client.nflpooldb
collection = db[year]
collection.insert(tiebreaker)

https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular/cumulative_player_stats.json?position=LB,SS,DT,DE,CB,FS,SS&playerstats=Sacks

https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular/cumulative_player_stats.json?position=QB,RB,WR,TE,CB,FS,SS,DE,DT,LB&playerstats=Sacks,
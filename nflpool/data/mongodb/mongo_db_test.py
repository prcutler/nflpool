import requests
from bson import json_util
from requests.auth import HTTPBasicAuth
from pymongo import MongoClient
import json
import nflpool.data.secret


#active_players = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/active_players.json',
#                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

#data = active_players.json()

#client = MongoClient('localhost', 27017)
#db = client.nflpooldb
#collection = db['2016']
#collection.insert(data)

#conference_standings = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular/conference_team_standings.json',
#                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

#conference = conference_standings.json()

#client = MongoClient('localhost', 27017)
#db = client.nflpooldb
#collection = db['2016']
#collection.insert(conference)


import requests
from bson import json_util
from requests.auth import HTTPBasicAuth
from pymongo import MongoClient
import json
import secret


response = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/active_players.json',
                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

data = response.json()

client = MongoClient('localhost', 27017)
db = client['nflpooldb']
collection = db['2016']['nfl_players']
collection.insert(data)

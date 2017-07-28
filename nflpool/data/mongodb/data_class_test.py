import mongoengine
import nflpool.data.secret
from pymongo import MongoClient
import requests
from requests.auth import HTTPBasicAuth
import json


#class Tiebreaker(mongoengine.EmbeddedDocument):
#    tiebreaker = mongoengine.DynamicField()


#class Season(mongoengine.Document):
#    year = mongoengine.EmbeddedDocument()


#class Stats(mongoengine.EmbeddedDocument):
#    tiebreaker = mongoengine.DynamicField()
#    individual = mongoengine.DynamicField()
#    conference = mongoengine.DynamicField()
#    division = mongoengine.DynamicField()

#client = MongoClient('localhost', 27017)
#mongoengine.connect('nflpooldb', alias='default')
#db = client.nflpooldb
#collection = db['Season']

#year = Season(2016)
#year.save()
#collection.insert(year)

#tiebreaker_data = requests.get('https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular'
#                               '/overall_team_standings.json?teamstats=Kickoff%20Returns.TD,Punt%20Returns.TD',
#                               auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

#tiebreaker_json = tiebreaker_data.json()

#tiebreaker_json = Stats(Tiebreaker())
#tiebreaker_json.save()


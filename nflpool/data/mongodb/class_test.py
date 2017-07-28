import requests
from requests.auth import HTTPBasicAuth
from pymongo import MongoClient
import nflpool.data.secret
import mongoengine


# Create a class for the collection
#class Season(mongoengine.Document):
#    season = mongoengine.EmbeddedDocument()
#    player_picks = mongoengine.EmbeddedDocument()

#    meta = {
#        'db_alias': 'core',
#        'collection': 'data'
#    }


# Create a class for the season week and embed in the Season
#class Week(mongoengine.EmbeddedDocument):
#    week = mongoengine.IntField()

#    meta = {
#        'db_alias': 'core',
#        'collection': 'data'
#    }


# Create a class for the stats to be embedded in each Week
#class Stats(mongoengine.EmbeddedDocument):
#    tiebreaker = mongoengine.EmbeddedDocument()

#    meta = {
#        'db_alias': 'core',
#        'collection': 'data'
#    }

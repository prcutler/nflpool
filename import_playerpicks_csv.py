import csv
import collections
from collections import namedtuple

nfl_pool_players = []
player_picks = ()

with open('json/2016_playerpicks.csv') as infile:
    reader = csv.DictReader(infile)
    picks = collections.namedtuple('picks', reader.fieldnames)
    player_picks = [picks(**row) for row in reader]

print(player_picks[0])

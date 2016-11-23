import requests
from requests.auth import HTTPBasicAuth
import secret
import json

response = requests.get(
    'https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/cumulative_player_stats.json',
    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

rawdata = response.content
data = json.loads(rawdata.decode())
headers = response.headers

player_list = data['cumulativeplayerstats']['playerstatsentry']

maxyds = 0
maxplayerid = 0
maxplayer = ''

top_rushers = []

for rushing in player_list:
    try:
        rushing_yards = rushing['stats']['RushYards']['#text']
        player_id = rushing['player']['ID']
        player_firstname = rushing['player']['FirstName']
        player_lastname = rushing['player']['LastName']
        player_position = rushing['player']['Position']
        if int(rushing_yards) > maxyds:
            maxyds = int(rushing_yards)
            maxplayerid = int(player_id)
            maxplayer = (player_firstname) + ' ' + (player_lastname)

        print((player_id), (player_firstname), (player_lastname), rushing_yards)

    except KeyError:
        continue

print(maxplayer, "with ", maxyds, "yds")

# TODO: Capture 1st, 2nd, 3rd, and 4th place player stats

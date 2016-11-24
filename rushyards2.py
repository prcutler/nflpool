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

maxrushers = []
v = 0

for rushing in player_list:
    try:
        rushing_yards = int(rushing['stats']['RushYards']['#text'])
        player_id = rushing['player']['ID']
        player_firstname = rushing['player']['FirstName']
        player_lastname = rushing['player']['LastName']
        player_position = rushing['player']['Position']

        print((player_id), (player_firstname), (player_lastname), rushing_yards)

        if v == 0:
            name = player_firstname + ' ' + player_lastname
            maxrushers.append([rushing_yards, name])
        elif v < 3:
            i = 0
            while i < len(maxrushers):
                if maxrushers[i][0] <= rushing_yards:
                    # insert before this one (so in this spot since everything will shift)
                    name = player_firstname + ' ' + player_lastname
                    maxrushers.insert(i, [rushing_yards, name])
                    i = len(maxrushers)
                i = i + 1
            if i > len(maxrushers):
                # smallest, just stick on the end since we don't have three yet
                name = player_firstname + ' ' + player_lastname
                maxrushers.append([rushing_yards, name])

        if v > 2:
            # already have at least three things in list, see if this is greater or equal to what's there
            i = 0
            while i < len(maxrushers):
                if maxrushers[i][0] <= rushing_yards:
                    # insert before this one (so in this spot since everything will shift)
                    name = player_firstname + ' ' + player_lastname
                    maxrushers.insert(i, [rushing_yards, name])
                    i = len(maxrushers)
                i = i + 1
            checkties = 1
            j = 2
            while len(maxrushers) > 3 and (checkties):
                if maxrushers[j][0] != maxrushers[j + 1][0]:
                    maxrushers.pop(j + 1)
                else:
                    checkties = 0

        v = v + 1


    except KeyError:
        continue

# print(maxplayer, "with ", maxyds, "yds")

# TODO: Capture 1st, 2nd, 3rd, and 4th place player stats

print(maxrushers)

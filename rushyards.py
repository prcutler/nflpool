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

rushing_yards_first = 0
rushing_yards_second = 0
rushing_yards_third = 0
rushing_yards_fourth = 0

rushing_yards_first_playerid = ''
rushing_yards__second_playerid = ''
rushing_yards__third_playerid = ''
rushing_yards_fourth_playerid = ''

rushing_yards_first_player = 0
rushing_yards_second_player = 0
rushing_yards_third_player = 0
rushing_yards_fourth_player = 0

top_rusher = [{"lastname": "Cutler"}, {"firstname": "Paul"}, {"ID": 123456}, {"yards": 1083}]

top_rushers = []

for rushing in player_list:
    try:
        rushing_yards = rushing['stats']['RushYards']['#text']
        player_id = rushing['player']['ID']
        player_firstname = rushing['player']['FirstName']
        player_lastname = rushing['player']['LastName']
        player_position = rushing['player']['Position']
        if int(rushing_yards) > maxyds:
            rushing_yards_first = int(rushing_yards)
            rushing_yards_first_playerid = int(player_id)
            rushing_yards_first_player = (player_firstname) + ' ' + (player_lastname)
        elif int(rushing_yards) >

        # print((player_id), (player_firstname), (player_lastname), rushing_yards)

        if (num1 > num2) and (num1 > num3):
            largest = num1
        elif (num2 > num1) and (num2 > num3):
            largest = num2
        else:
            largest = num3

    except KeyError:
        continue

    print(type(rushing_yards))
    print(type(player_lastname))

print(maxplayer, "with ", maxyds, "yds")


# TODO: Capture 1st, 2nd, 3rd, and 4th place player stats

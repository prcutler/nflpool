import requests
from requests.auth import HTTPBasicAuth
import secret
import json

x = 0
y = 0

parameters = 'teamstats'

response = requests.get(
    'https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/playoff_team_standings.json?teamstats',
    auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

rawdata = response.content
data = json.loads(rawdata.decode())

teamlist = data["playoffteamstandings"]["conference"][0]["teamentry"]

for afc_team_list in teamlist:
    afc_team_name = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["Name"]
    afc_team_city = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["City"]
    afc_team_id = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["ID"]
    afc_team_abbr = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["team"]["Abbreviation"]
    afc_rank = data["playoffteamstandings"]["conference"][0]["teamentry"][x]["rank"]
    print((afc_team_name), (afc_team_city), (afc_team_id), (afc_team_abbr), afc_rank)
    x = x + 1

for nfc_team_list in teamlist:
    nfc_team_name = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["Name"]
    nfc_team_city = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["City"]
    nfc_team_id = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["ID"]
    nfc_team_abbr = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["team"]["Abbreviation"]
    nfc_rank = data["playoffteamstandings"]["conference"][1]["teamentry"][y]["rank"]
    y = y + 1
    print((nfc_team_name), (nfc_team_city), (nfc_team_id), (nfc_team_abbr), nfc_rank)

import requests
from requests.auth import HTTPBasicAuth
import secret

parameters = 'teamstats'

response = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/playoff_team_standings.json?teamstats',
                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

print(response.status_code)

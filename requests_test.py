import requests
from requests.auth import HTTPBasicAuth
import secret


response = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/division_team_standings.json',
             auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

print(response.status_code)
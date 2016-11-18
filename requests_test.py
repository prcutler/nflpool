import requests
from requests.auth import HTTPBasicAuth
import secret

parameters = 'teamstats'

response = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/playoff_team_standings.json?teamstats',
                        auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

print(response.status_code)

# Make a get request with the parameters.
#response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

#https://www.mysportsfeeds.com/api/feed/pull/nfl/{2016-2017}/playoff_team_standings.json
#{format}?teamstats={team-stats}
#https://www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017/playoff_team_standings.json
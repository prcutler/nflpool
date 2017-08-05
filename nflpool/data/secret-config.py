# You will need an account from MySportsFeed to access their API.  They offer free access to developers
# Edit below with your credentials and then save as secret.py

msf_username = 'YOURUSERNAME'
msf_pw = 'YOURPASSWORD'

msf_url = ''

# response = requests.get(
#            'https://api.mysportsfeeds.com/v1.1/pull/nfl/2016-2017-regular/conference_team_standings.json',
    #            auth=HTTPBasicAuth(secret.msf_username, secret.msf_pw))

# Get the current season to use in all JSON request URLs
#session = DbSessionFactory.create_session()
#season = session.query(SeasonInfo).filter(SeasonInfo.id == '1').first()
#print(season)


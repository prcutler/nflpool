import json

# Change the name of the file to open to match the query below:
with open('json/20161018-playoff-team-standings.json') as file:
    alltext = file.readlines()  # Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

        for conference in data['playoffteamstandings']['conference']:
            print(conference['@name'])
            for team in conference['teamentry']:
                print(team['team']['ID'], team['rank'])
            print('')

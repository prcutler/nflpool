import json

# Change the name of the file to open to match the query below:
with open('json/20160921-division-team-standings.json') as file:
    alltext = file.readlines()  # Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

        for division in data['divisionteamstandings']['division']:
            print(division['@name'])
            for team in division['teamentry']:
                print(team['team']['ID'], team['rank'])
            print('')

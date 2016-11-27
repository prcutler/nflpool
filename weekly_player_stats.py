import json

# Change the name of the file to open to match the query below:
with open('json/20161018-cumulative-player-stats.json') as file:
    alltext = file.readlines()  # Put each line into a list


for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

        player_list = data['cumulativeplayerstats']['playerstatsentry']

        for rushing in player_list:
            try:
                rushing_yards = rushing['stats']['RushYards']['#text']
                player_id = rushing['player']['ID']
                player_firstname = rushing['player']['FirstName']
                player_lastname = rushing['player']['LastName']
                player_position = rushing['player']['Position']
                print((player_id), (player_firstname), (player_lastname), rushing_yards)

            except KeyError:
                continue

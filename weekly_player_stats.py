import json

# Change the name of the file to open to match the query below:
with open('json/20161018-cumulative-player-stats.json') as file:
    alltext = file.readlines()  # Put each line into a list

v = 0  # Rushing
w = 0  # Receiving
x = 0  # Passing
y = 0  # Sacks
z = 0  # Interceptions

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

        for rushing in data:
            rushing_yards = data['cumulativeplayerstats']['playerstatsentry'][v]['stats']['RushYards']['#text']
            player_id = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['ID']
            player_firstname = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['FirstName']
            player_lastname = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['LastName']
            player_position = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['Position']
            print((player_id), (player_firstname), (player_lastname), rushing_yards)
            v += 1

            #            rushing_yards = data['cumulativeplayerstats']['playerstatsentry'][6]['stats']['RushYards']['#text']
            #            player_id = data['cumulativeplayerstats']['playerstatsentry'][6]['player']['ID']
            #            player_firstname = data['cumulativeplayerstats']['playerstatsentry'][6]['player']['FirstName']
            #            player_lastname = data['cumulativeplayerstats']['playerstatsentry'][6]['player']['LastName']
            #            player_position = data['cumulativeplayerstats']['playerstatsentry'][6]['player']['Position']
            #            print((player_id), (player_firstname), (player_lastname), rushing_yards)

            rushing_yards = data['cumulativeplayerstats']['playerstatsentry'][6]['stats']
            print(rushing_yards)

            # TODO: Either do query based on position or write an if / elif statement or try / except if Key Error returned

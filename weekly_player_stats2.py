import json

# Change the name of the file to open to match the query below:
with open('json/20161018-cumulative-player-stats.json') as file:
    alltext = file.readlines()  # Put each line into a list

for lines in alltext:
    if lines.startswith('{'):
        rawdata = lines
        data = json.loads(rawdata)

        player_list = data['cumulativeplayerstats']['playerstatsentry']

        # try:
        #    for rushing in player_list:
        #        rushing_yards = data['cumulativeplayerstats']['playerstatsentry'][v]['stats']['RushYards']['#text']
        #        player_id = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['ID']
        #        player_firstname = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['FirstName']
        #        player_lastname = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['LastName']
        #        player_position = data['cumulativeplayerstats']['playerstatsentry'][v]['player']['Position']
        #        print((player_id), (player_firstname), (player_lastname), rushing_yards)
        # except KeyError:


        maxyds = 0
        maxplayerid = 0
        maxplayer = ''

        for rushing in player_list:
            try:
                rushing_yards = rushing['stats']['RushYards']['#text']
                player_id = rushing['player']['ID']
                player_firstname = rushing['player']['FirstName']
                player_lastname = rushing['player']['LastName']
                player_position = rushing['player']['Position']
                if int(rushing_yards) > maxyds:
                    maxyds = int(rushing_yards)
                    maxplayerid = int(player_id)
                    maxplayer = (player_firstname) + ' ' + (player_lastname)

                print((player_id), (player_firstname), (player_lastname), rushing_yards)

            except KeyError:
                continue

        print("maxplayer=", (maxplayer), "with ", (maxyds), "yds")

        #        rushing_yards = data['cumulativeplayerstats']['playerstatsentry'][1]['stats']['RushYards']['#text']
        #        player_id = data['cumulativeplayerstats']['playerstatsentry'][1]['player']['ID']
        #        player_firstname = data['cumulativeplayerstats']['playerstatsentry'][1]['player']['FirstName']
        #        player_lastname = data['cumulativeplayerstats']['playerstatsentry'][1]['player']['LastName']
        #        player_position = data['cumulativeplayerstats']['playerstatsentry'][1]['player']['Position']
        #        print((player_id), (player_firstname), (player_lastname), rushing_yards)

        #            rushing_yards = data['cumulativeplayerstats']['playerstatsentry'][6]['stats']
        #            print(rushing_yards)

        # TODO: Either do query based on position or write an if / elif statement or try / except if Key Error returned

import json


def main():
    stats()


def individual_stats():
    for stats in player_list:
        try:
            rushing_yards = stats['stats']['RushYards']['#text']
            passing_yards = stats['stats']['PassYards']['#text']
            receiving_yards = stats['stats']['RecYards']['#text']
            interceptions = stats['stats']['Interceptions']['#text']
            sacks = stats['stats']['Sacks']['#text']
            player_id = stats['player']['ID']
            player_firstname = stats['player']['FirstName']
            player_lastname = stats['player']['LastName']
            player_position = stats['player']['Position']
        #            print((player_id), (player_firstname), (player_lastname), rushing_yards)

        # TODO: Add SQL code to add data to database for each statistical category

        except KeyError:
            continue



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

if __name__ == '__main__':
    main()

import json


def main():
    filename = get_data()
    data = load_file(filename)
    individual_stats(data)


def get_data():
    # Change the name of the file to open to match the query below:
    with open('json/20161018-cumulative-player-stats.json') as file:
        alltext = file.readlines()  # Put each line into a list


def load_file(filename):

    for lines in alltext:
        if lines.startswith('{'):
            rawdata = lines
            all_stats = json.loads(rawdata)

            player_list = all_stats['cumulativeplayerstats']['playerstatsentry']

            return player_list
#
#            for rushing in player_list:
#                try:
#                    rushing_yards = rushing['stats']['RushYards']['#text']
#                    player_id = rushing['player']['ID']
#                    player_firstname = rushing['player']['FirstName']
#                    player_lastname = rushing['player']['LastName']
#                    player_position = rushing['player']['Position']
#                    print((player_id), (player_firstname), (player_lastname), rushing_yards)
#
#                except KeyError:
#                    continue


def individual_stats(data):
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
            print(player_id, player_firstname, player_lastname, player_position, rushing_yards)

        # TODO: Add SQL code to add data to database for each statistical category

        except KeyError:
            continue


if __name__ == '__main__':
    main()
